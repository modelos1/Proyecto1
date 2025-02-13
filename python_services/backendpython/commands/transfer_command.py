"""
This module is responsible for the commands to transfer money.

author: Julian David Pulido Carreño  <judpulidoc@udistrtital.edu.co>

This file is part of Proyecto1.
"""

# pylint: disable=import-error
from datetime import datetime
from repositories.transfer import TransferDAO
from repositories.transfer import TransferRepository
from repositories.account import AccountRepository
from commands.command import Command
from fastapi import HTTPException
from observers.transaction_subject import TransactionSubject
from observers.notification_observer import NotificationObserver
from observers.log_observer import LogObserver


class TransferCommand(Command):
    """This class is used to manage the transfer of money."""

    def __init__(self, number_sender: str, number_receiver: str, amount: float):
        self.number_sender = number_sender
        self.number_receiver = number_receiver
        self.amount = amount
        self.account_repository = AccountRepository()
        self.transfer_repository = TransferRepository()
        
        # Create the subject and attach the observers
        self.transaction_subject = TransactionSubject()
        self.transaction_subject.attach(LogObserver())
        self.transaction_subject.attach(NotificationObserver())

    def execute(self):
        """This method is used to execute the command of the transfer."""
        sender_account = self.account_repository.get_actual_account(self.number_sender)
        receiver_account = self.account_repository.get_actual_account(
            self.number_receiver
        )

        if sender_account is None:
            raise HTTPException(
                status_code=404, detail="The sender account does not exist."
            )
        if receiver_account is None:
            raise HTTPException(
                status_code=404, detail="The receiver account does not exist."
            )
        if sender_account.balance < self.amount:
            raise HTTPException(
                status_code=400, detail="The sender account does not have enough money."
            )

        self.account_repository.update_balance(
            self.number_sender, self.amount, "withdraw"
        )
        self.account_repository.update_balance(
            self.number_receiver, self.amount, "deposit"
        )

        transfer = TransferDAO(
            sender=self.number_sender,
            receiver=self.number_receiver,
            amount=self.amount,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status="completed",
        )
        self.transfer_repository.create_transfer(transfer, "transfer")

        # Notify the observers
        transaction_data = {
            "type": "transfer",
            "sender": self.number_sender,
            "receiver": self.number_receiver,
            "amount": self.amount,
            "timestamp": transfer.timestamp,
            "status": transfer.status,
        }
        self.transaction_subject.notify(transaction_data)

        return "The money has been transferred successfully."
