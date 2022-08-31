
# let's be bankers!
# this is a very simplified digital bank handling transactions
def main():

    # list of transactions where each transaction is a tuple with format (sender account number, receiver account number, amount)
    transaction_list = [
        (1152, 1978, 550),
        (8736, 1765, 850),
        (1978, 8312, 700),
        (1152, 5763, 350),
        (1765, 8145, 650),
        (5106, 1730, 300),
        (5398, 1978, 250)
    ]

    # we will assume this bank is a clearing bank that also handles transactions between other banks
    # the different banks are identified by the first digit in the account number.
    # accounts starting with 1 is this bank, other accounts are other banks

    # this bank has an overview of balance for its customers, but not for other banks
    internal_account_balance = {
        1152: 750,
        1978: 1200,
        1765: 350,
        1730: 200
    }

    # other banks will be sent info on the change to their accounts. This data is initialized
    external_account_balance = {}

    # accounts can be overdrawn a bit, but will block the transaction if sender account is overdrawn too much
    # these rejected transactions must be stored. This can only be done for internal accounts
    rejected_transfers = []

    # the government is interested in who sends money to whom, and requests and overview of accounts that interact with each other
    connections_dict = {}

    # iterate over transactions lists
    for transaction in transaction_list:

        # extract the different data
        sender = transaction[0]
        receiver = transaction[1]
        amount = transaction[2]

        # calls custom func to populate these three outputs
        internal_account_balance, external_account_balance, rejected_transfers = process_transaction(
            sender=sender, receiver=receiver, amount=amount, internal_account_balance=internal_account_balance,
            external_account_balance=external_account_balance, rejected_transfers=rejected_transfers
        )

        connections_dict = make_connections_overview(sender=sender, receiver=receiver, connections_dict=connections_dict)

    print("\nInternal account balance:")
    print(internal_account_balance)

    print("\nExternal account balance:")
    print(external_account_balance)

    print("\nRejected transactions:")
    print(rejected_transfers)

    print("\nAccount connections:")
    print(connections_dict)


def process_transaction(sender, receiver, amount, internal_account_balance, external_account_balance,
                        rejected_transfers, overdraw_limit=100):
    """
        Function for processing transactions.
        Estimates the account balances for each transaction.
        For internal account validation of account coverage for transaction is done. Rejections are recorded.

        For simplicity, we assume all external account will have coverage to do all transfers.

        Args:
            sender(int):
            Sender ID of transaction sender

            receiver(int):
            Receiver ID of transaction receiver

            amount(int):
            Amount in transaction

            internal_account_balance(dict(key=account_number(int), value=current_account_total(int)):
            The account total for internal customers.

            external_account_balance(dict(key=bank_in(int), value=(
                                    key=account_number(int), value=current_account_total(int)):
            The account total for internal customers.
            A nested dict where first level is bank ID, and next level is account amount

            rejected_transfers(list):
            List with rejected transactions

            overdraw_limit(int, optional)

        Returns:
             internal_account_balance(dict(key=account_number(int), value=current_account_total(int)):
            The account total for internal customers.

            external_account_balance(dict(key=bank_in(int), value=(
                                    key=account_number(int), value=current_account_total(int)):
            The account total for internal customers.
            A nested dict where first level is bank ID, and next level is account amount

            rejected_transfers(list):
            List with rejected transactions
        """

    # extract bank ID from sender and receiver
    sender_bank = str(sender)[0]
    receiver_bank = str(receiver)[0]

    # initialize a rejection flag
    rejected_transaction = False

    # checks if sender is internal
    if sender_bank == "1":

        # checks if sender has coverage for transaction
        if internal_account_balance[sender]-amount >= -overdraw_limit:
            internal_account_balance[sender] -= amount
        else:
            rejected_transaction = True
            rejected_transfers.append(f"Transaction of {amount} NOK to {receiver} was rejected for account {sender}")

    # if account is in external bank
    else:
        # checks if external bank is in dict
        if sender_bank in external_account_balance:

            # checks if sender is in dict value of external bank
            if sender in external_account_balance[sender_bank]:
                external_account_balance[sender_bank][sender] -= amount
            else:
                external_account_balance[sender_bank][sender] = amount

        # if bank is not in dict, we also know that this account will be the only one so far for this bank
        else:
            external_account_balance[sender_bank] = {sender: amount}

    # if transaction is rejected, receiver will not have account amount changed
    if not rejected_transaction:

        if receiver_bank == "1":
            internal_account_balance[receiver] += amount
        else:

            # checks if external bank is in dict
            if receiver_bank in external_account_balance:

                # checks if sender is in dict value of external bank
                if receiver in external_account_balance[receiver_bank]:
                    external_account_balance[receiver_bank][receiver] -= amount
                else:
                    external_account_balance[receiver_bank][receiver] = amount

    # returns the output
    return internal_account_balance, external_account_balance, rejected_transfers


def make_connections_overview(sender, receiver, connections_dict):
    """
            Function for making overview of all the connections between accounts

            Args:
                sender(int):
                Sender ID of transaction sender

                receiver(int):
                Receiver ID of transaction receiver

                connections_dict(dict(key=account_id(int), value=connections(set))):
                Dict with one key-value pair for each unique account in transaction list.
                The values are sets with account numbers.

            Returns:
                connections_dict(dict(key=account_id(int), value=connections(set))):
                Dict with one key-value pair for each unique account in transaction list.
                The values are sets with account numbers.

    """

    # checks if sender is already in connections_dict
    if sender in connections_dict:
        # appends receiver to sender's set
        connections_dict[sender].add(receiver)
    else:
        # creates a new set for the sender
        connections_dict[sender] = {receiver}

    # similar logic to that of sender
    if receiver in connections_dict:
        connections_dict[receiver].add(sender)
    else:
        connections_dict[receiver] = {sender}

    return connections_dict


if __name__=="__main__":
    main()