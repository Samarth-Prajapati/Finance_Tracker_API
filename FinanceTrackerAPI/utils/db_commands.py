from FinanceTrackerAPI.utils import transactions

class Transactions:
    def __init__(self):
        self.transactions = transactions

    def create_transactions(self, data):
        """
        Add transaction in Transaction Collection
        :return: transaction data
        """

        try:
            result = self.transactions.insert_one(data)
            return result

        except Exception as error:
            print("Error while creating transaction,", error)

    def get_transactions(self):
        """
        Get transaction data
        :return: all transaction data
        """

        try:
            result = self.transactions.find({}, {"_id" : 0})
            return result

        except Exception as error:
            print("Error while fetching all transactions,", error)

transactions_commands = Transactions()