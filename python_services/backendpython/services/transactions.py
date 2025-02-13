"""
This module id used to handle services related to transactions.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>

This file is part of Proyecto1.



"""

# pylint: disable=import-error
from datetime import datetime
from typing import List
from fastapi import HTTPException
from repositories.transactions import TransactionsRepository, TransactionsDAO


class TransactionsService:
    """this class has the transactions services."""

    def __init__(self):
        """This method is used to initialize the class (constructor)."""
        self.transactions_repository = TransactionsRepository()

    def get_transactions(self) -> List[TransactionsDAO]:
        """This method is used to get all transactions.

        Returns:
            List[TransactionsDAO]: A list of transactions.
        """
        return self.transactions_repository.get_transactions()

    def get_transaction_by_owner(self, transaction_owner: str) -> TransactionsDAO:
        """This method is used to get a transaction by owner.

        Args:
            transaction_owner (str): The id of the transaction.

        Returns:
            TransactionsDAO: The transaction.
        """
        transactions = []
        for transaction in self.transactions_repository.get_transactions():
            if transaction.owner == transaction_owner:
                transactions.append(transaction)

        if not transactions:
            raise HTTPException(status_code=404, detail="Transaction not found")

        return transactions

    def get_transactions_by_type(self, transaction_type: str) -> List[TransactionsDAO]:
        """This method is used to get transactions by type.

        Args:
            transaction_type (str): The type of the transaction.

        Returns:
            List[TransactionsDAO]: A list of transactions.
        """
        response = []

        for transaction in self.transactions_repository.get_transactions():
            if transaction_type.lower() == transaction.type.lower():
                response.append(transaction)
        return response

    def create_transaction(self, transaction: TransactionsDAO) -> TransactionsDAO:
        """This method is used to create a transaction.

        Args:
            transaction (TransactionsDAO): The transaction to create.

        Returns:
            TransactionsDAO: The created transaction.
        """
        return self.transactions_repository.create_transaction(transaction)

    def get_transactions_by_date(
        self, transaction_date_start: datetime, transaction_date_end: datetime
    ) -> List[TransactionsDAO]:
        """This method is used to get transactions by date.

        Args:
            transaction_date_start (str): The start date of the transaction.
            transaction_date_end (str): The end date of the transaction.

        Returns:
            List[TransactionsDAO]: A list of transactions.
        """
        response = []
        if isinstance(transaction_date_start, str) and isinstance(transaction_date_end, str):
            for transaction in self.transactions_repository.get_transactions():
                transaction_date_start = datetime.strptime(
                    transaction_date_start, "%Y-%m-%d"
                )
                transaction_date_end = datetime.strptime(transaction_date_end, "%Y-%m-%d")
                transaction.timestamp = datetime.strptime(
                    transaction.timestamp, "%Y-%m-%d"
                )
                if transaction_date_start <= transaction.timestamp <= transaction_date_end:
                    response.append(transaction)
        else:
            raise HTTPException(
                status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'"
            )
        return response
