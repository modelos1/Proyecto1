"""
This module is used to interact with data from Transactions in json format.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>

"""

import json
from datetime import datetime
from typing import List
from pydantic import BaseModel
from environment_variables import EnvironmentVariables


class TransactionsDAO(BaseModel):
    """This class is used to represent the transaction data."""

    owner: str
    amount: float
    timestamp: str
    type: str
    status: str


class TransactionsRepository:
    """ "This class is used to interact with the data from the transactions."""

    def __init__(self):
        """This method is used to initialize the class (constructor)."""
        path_file = EnvironmentVariables().path_transactions_data
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        """This method is used to load the data from a file."""
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
                if not isinstance(self.data, dict) or "transactions" not in self.data:
                    self.data = {"transactions": []}
        except Exception as e:
            print(e)
            self.data = []

    def _save_data(self):
        """This method is used to save the data to a file."""
        path_file = EnvironmentVariables().path_transactions_data
        with open(path_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def get_transactions(self) -> List[TransactionsDAO]:
        """This method is used to get all transactions."""
        self._load_data(EnvironmentVariables().path_transactions_data)
        transactions = []
        if isinstance(self.data, dict) and "transactions" in self.data:
            transactions_list = self.data["transactions"]  # Extract transactions list
        else:
            print("Error: transactions data not found or invalid format.")
            return []

        for transaction in transactions_list:
            if isinstance(transaction, dict):  # Verify dictionary format
                try:
                    transactions.append(
                        TransactionsDAO(
                            owner=transaction.get("owner", "Unknown"),
                            amount=transaction.get("amount", 0.0),
                            timestamp=transaction.get(
                                "timestamp", datetime.now().isoformat()
                            ),
                            type=transaction.get("type", "undefined"),
                            status=transaction.get("status", "pending"),
                        )
                    )
                except Exception as e:
                    print(f"Skipping invalid transaction: {transaction}, Error: {e}")
            else:
                print(f"Invalid transaction format: {transaction}")

        return transactions

    def create_transaction(self, transaction: TransactionsDAO) -> TransactionsDAO:
        """This method is used to create a transaction."""
        self._load_data(EnvironmentVariables().path_transactions_data)
        self.data["transactions"].append(transaction.model_dump())
        self._save_data()
        return transaction
