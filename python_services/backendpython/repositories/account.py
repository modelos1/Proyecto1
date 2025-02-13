"""
This file contains the class that will be used to interact with the data in json format.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>

This file is part of Proyecto1.

"""

import json
from pydantic import BaseModel
from environment_variables import EnvironmentVariables


class ActualAccountDAO(BaseModel):
    """This class has the actual account."""

    account_number: str
    balance: float


class AccountRepository:
    """This class is used to interact with the data from the account."""

    def __init__(self):
        """This method is used to initialize the class (constructor)."""
        path_file = EnvironmentVariables().path_account_data
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        """This method is used to load the data from a file."""
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
            print("Data loaded successfully.")
        except Exception as e:
            print(e)
            self.data = []

    def save_data(self):
        """This method is used to save the data to a file."""
        path_file = EnvironmentVariables().path_account_data
        with open(path_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def get_actual_account(self, phone_number: str) -> ActualAccountDAO:
        """This method is used to get the actual account."""
        self._load_data(EnvironmentVariables().path_account_data)
        if isinstance(self.data, dict) and "accounts" in self.data:
            accounts_list = self.data["accounts"]
        else:
            print("Error: accounts data not found or invalid format.")
            return None
        for account in accounts_list:
            if str(account["account_number"]) == str(phone_number):
                return ActualAccountDAO(
                    account_number=account.get("account_number", "Unknown"),
                    balance=account.get("balance", 0.0),
                )
        print("Error: account not found.")
        return None

    def update_balance(self, phone_number: str, amount: float, type_transaction: str):
        """This method is used to update the balance of the account."""
        self._load_data(EnvironmentVariables().path_account_data)
        if isinstance(self.data, dict) and "accounts" in self.data:
            accounts_list = self.data["accounts"]
        else:
            print("Error: accounts data not found or invalid format.")
            return []
        for account in accounts_list:
            if account["account_number"] == phone_number:
                if type_transaction == "deposit":
                    account["balance"] = account["balance"] + amount
                elif type_transaction == "withdraw":
                    account["balance"] = account["balance"] - amount
                self.save_data()
                break
