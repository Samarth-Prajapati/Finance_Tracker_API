from FinanceTrackerAPI.utils import transactions
from bson import ObjectId

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

    def get_transactions_id(self, obj_id):
        """
        Get data using id
        :param obj_id: transaction_id
        :return: transaction data of specified transaction id
        """

        try:
            result = self.transactions.find_one({"_id" : ObjectId(obj_id)}, {"_id" : 0})
            return result

        except Exception as error:
            print("Error while fetching transaction,", error)

    def delete_transaction(self, obj_id):
        """
        Delete transaction
        :param obj_id: transaction id
        :return: None
        """

        try:
            self.transactions.delete_one({"_id" : ObjectId(obj_id)})
            return True

        except Exception as error:
            print("Error while deleting transaction,", error)

    def delete_transaction_bulk(self, category):
        """
        Delete transaction in bulk
        :param category: category of transaction
        :return: None
        """

        try:
            self.transactions.delete_many({"category": str(category)})
            return True

        except Exception as error:
            print("Error while deleting transaction,", error)

    def update_transaction(self, obj_id, data):
        """
        Update transaction
        :param obj_id: transaction_id
        :param data: updated data
        :return: updated transaction data
        """
        try:
            result = self.transactions.update_one({"_id": ObjectId(obj_id)}, {"$set": data})

            if result.matched_count == 0:
                return None

            return self.transactions.find_one({"_id" : ObjectId(obj_id)}, {"_id" : 0})

        except Exception as error:
            print("Error while deleting transaction,", error)

transactions_commands = Transactions()