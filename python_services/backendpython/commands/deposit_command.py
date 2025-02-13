"""
This module is the command to deposit money in the account.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>

This file is part of Proyecto1.


"""
# pylint: disable=import-error
from datetime import datetime
from repositories.transactions import TransactionsRepository, TransactionsDAO
from repositories.account import AccountRepository
from commands.command import Command
from observers.transaction_subject import TransactionSubject
from observers.notification_observer import NotificationObserver
from observers.log_observer import LogObserver

class DepositCommand(Command):
    """This class is used to deposit money in the account."""
    def __init__(self, account_number:str, amount:float):
        self.number = account_number
        self.amount = amount
        self.account_repository = AccountRepository()
        self.transaction_repository = TransactionsRepository()

        # Create the subject and attach the observers
        self.transaction_subject = TransactionSubject()
        self.transaction_subject.attach(LogObserver())
        self.transaction_subject.attach(NotificationObserver())

    def execute(self):
        """This method is used to execute the command of the deposit and notify the observers."""
        self.account_repository.update_balance(self.number, self.amount, "deposit")
        self.account_repository.save_data()
        transaction = TransactionsDAO(
            owner=self.number,
            amount=self.amount,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            type="deposit",
            status="completed"
        )
        self.transaction_repository.create_transaction(transaction)

        # Notify the observers
        transaction_data = {
            "type": "deposit",
            "amount": self.amount,
            "owner": self.number,
            "timestamp": transaction.timestamp,
            "status": "completed"
        }
        self.transaction_subject.notify(transaction_data)

        return "The money has been deposited successfully."
    