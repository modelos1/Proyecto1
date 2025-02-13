"""This module is use to handle services related to transfers."""

# pylint: disable=import-error
from fastapi import HTTPException
from repositories.account import AccountRepository
from repositories.transfer import TransferRepository, TransferDAO
from commands.transfer_command import TransferCommand
from commands.withdraw_command import WithdrawCommand
from commands.deposit_command import DepositCommand


class TransferService:
    """this class has the transfers services."""

    def __init__(self):
        """This method is used to initialize the class (constructor)."""
        self.transfer_repository = TransferRepository()
        self.account_repository = AccountRepository()

    def transfer_money(self, transfer: TransferDAO):
        """This method is used to transfer money between accounts using a command.

        Args:
            transfer (TransferDAO): The transfer object.
        """
        sender_account = transfer.sender
        receiver_account = transfer.receiver
        amount = transfer.amount

        if sender_account == receiver_account:
            raise HTTPException(
                status_code=400, detail="The sender and receiver accounts are the same."
            )
        if amount <= 0:
            raise HTTPException(
                status_code=400, detail="The amount must be greater than zero."
            )
        command = TransferCommand(sender_account, receiver_account, amount)
        return command.execute()

    def deposit_money(self, phone_number: str, amount: float):
        """This method is used to deposit money in an account."""
        if amount <= 0:
            raise HTTPException(
                status_code=400, detail="The amount must be greater than zero."
            )
        command = DepositCommand(phone_number, amount)
        return command.execute()

    def withdraw_money(self, phone_number: str, amount: float):
        """This method is used to withdraw money from an account."""
        if amount <= 0:
            raise HTTPException(
                status_code=400, detail="The amount must be greater than zero."
            )
        command = WithdrawCommand(phone_number, amount)
        return command.execute()
