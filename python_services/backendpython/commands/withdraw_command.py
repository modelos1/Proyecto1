"""
This module is the command to withdraw money from an account

author: Julian David Pulido Carreño  <judpulidoc@uditrital.edu.co>

This file is part of Proyecto1.

"""

# pylint: disable=import-error
from datetime import datetime
from repositories.transactions import TransactionsRepository, TransactionsDAO
from repositories.account import AccountRepository
from commands.command import Command
from fastapi import HTTPException
from observers.transaction_subject import TransactionSubject
from observers.notification_observer import NotificationObserver
from observers.log_observer import LogObserver


class WithdrawCommand(Command):
    """This class is used to wthdraw money from an account."""

    def __init__(self, account_number: str, amount: float):
        self.number = account_number
        self.amount = amount
        self.account_repository = AccountRepository()
        self.transaction_repository = TransactionsRepository()

        # Create the subject and attach the observers
        self.transaction_subject = TransactionSubject()
        self.transaction_subject.attach(LogObserver())
        self.transaction_subject.attach(NotificationObserver())

    def execute(self):
        """This method is used to execute the command."""
        account = self.account_repository.get_actual_account(self.number)
        if account is None:
            raise HTTPException(status_code=404, detail="The account does not exist.")
        if account.balance < self.amount:
            raise HTTPException(
                status_code=400, detail="The account does not have enough money."
            )
        self.account_repository.update_balance(self.number, self.amount, "withdraw")
        self.account_repository.save_data()

        transaction = TransactionsDAO(
            owner=self.number,
            amount=self.amount,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            type="withdraw",
            status="completed",
        )
        self.transaction_repository.create_transaction(transaction)

        # Notify the observers+
        transaction_data = {
            "type": "withdraw",
            "amount": self.amount,
            "owner": self.number,
            "timestamp": transaction.timestamp,
            "status": "completed",
        }
        self.transaction_subject.notify(transaction_data)

        return "The money has been withdrawn successfully."
