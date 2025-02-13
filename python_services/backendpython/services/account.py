"""
This module is use to handle services related to accounts.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>

This file is part of Proyecto1.

"""

from repositories.account import AccountRepository, ActualAccountDAO


class AccountService:
    """this class has the account services."""
    def __init__(self):
        """This method is used to initialize the class (constructor)."""
        self.account_repository = AccountRepository()

    def get_actual_account(self, phone_number:str) -> ActualAccountDAO:
        """This method is used to get the actual account.
        Returns:
            ActualAccount: The actual account.
        """
        return self.account_repository.get_actual_account(phone_number)
    
    def update_balance(self, phone_number:str, amount:float, type_transaction:str):
        """This method is used to update the balance of the account."""
        self.account_repository.update_balance(phone_number, amount, type_transaction)
    