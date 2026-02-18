from FinanceTrackerAPI.utils import transactions, categories
from bson import ObjectId
import datetime

class Transactions:
    def __init__(self):
        self.transactions = transactions

    def create_transactions(self, data):
        """
        Add transaction in Transaction Collection
        :return: transaction data
        """

        try:
            data["created_at"] = str(datetime.datetime.now())
            data["updated_at"] = None
            data["date"] = str(datetime.date.today())

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
            data["updated_at"] = str(datetime.datetime.now())
            result = self.transactions.update_one({"_id": ObjectId(obj_id)}, {"$set": data})

            if result.matched_count == 0:
                return None

            return self.transactions.find_one({"_id" : ObjectId(obj_id)}, {"_id" : 0})

        except Exception as error:
            print("Error while updating transaction,", error)

    def search_transactions(self, query):
        """
        Search transactions
        :param query: title or description string we want to search.
        :return: search results
        """

        try:
            search_filter = {
                "$or": [
                    {"title": {"$regex": query, "$options": "i"}},
                    {"description": {"$regex": query, "$options": "i"}},
                    {"category": {"$regex": query, "$options": "i"}}
                ]
            }
            return list(self.transactions.find(search_filter, {"_id" : 0}))

        except Exception as error:
            print("Error while searching transaction,", error)

class Categories:
    def __init__(self):
        self.categories = categories

    def create_categories(self, data):
        """
        Add category in Category Collection
        :param data : category_data
        :return: category data
        """


        try:
            data["created_at"] = str(datetime.datetime.now())
            result = self.categories.insert_one(data)
            return result

        except Exception as error:
            print("Error while creating category,", error)

    def get_categories(self):
        """
        Get category data
        :return: all category data
        """

        try:
            result = self.categories.find({}, {"_id" : 0})
            return result

        except Exception as error:
            print("Error while fetching all categories,", error)

    def delete_category(self, name):
        """
        Delete category
        :param name: category name
        :return: None
        """

        try:
            self.categories.delete_one({"name": str(name.lower())})
            return True

        except Exception as error:
            print("Error while deleting category,", error)

    def update_category(self, name, data):
        """
        Update category
        :param name: category name
        :param data: updated data
        :return: updated category data
        """

        try:
            result = self.categories.update_one({"name": str(name.lower())}, {"$set": data})

            if result.matched_count == 0:
                return None

            return self.categories.find_one({"name" : str(name.lower())}, {"_id" : 0})

        except Exception as error:
            print("Error while deleting category,", error)

transactions_commands = Transactions()
categories_commands = Categories()