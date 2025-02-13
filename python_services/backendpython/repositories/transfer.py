"""This module contains the repository of the transfer entity.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>

This file is part of Proyecto1.
"""

import json
from pydantic import BaseModel
from transactions import TransactionsDAO
# pylint: disable=import-error
from environment_variables import EnvironmentVariables


class TransferDAO(BaseModel):
    """This class is used to represent the transfer data."""

    sender: str
    receiver: str
    amount: float
    timestamp: str
    status: str


class TransferRepository:
    """This class is used to interact with the data from the transfers."""

    def __init__(self):
        """This method is used to initialize the class (constructor)."""
        path_file = EnvironmentVariables().path_transactions_data
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        """This method is used to load the data from a file."""
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(e)
            self.data = []

    def _save_data(self):
        """This method is used to save the data to a file."""
        path_file = EnvironmentVariables().path_transactions_data
        with open(path_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def create_transfer(self, transfer: TransferDAO, transaction_type: str):
        """This method is used to create a transfer."""
        if transaction_type == "transfer":
            transaction_sender = TransactionsDAO(
                owner=transfer.sender,
                amount=transfer.amount,
                timestamp=transfer.timestamp,
                type="transfer",
                status="completed",
            )
            transaction_receiver = TransactionsDAO(
                owner=transfer.receiver,
                amount=transfer.amount,
                timestamp=transfer.timestamp,
                type="transfer",
                status="completed",
            )
            self.data.append(transaction_sender.dict())
            self.data.append(transaction_receiver.dict())
            self._save_data()
        else:
            transaction_sender = TransactionsDAO(
                owner=transfer.sender,
                amount=transfer.amount,
                timestamp=transfer.timestamp,
                type="transfer",
                status="completed",
            )
            self.data.append(transaction_sender.dict())
            self._save_data()
        return "The transfer has been created successfully."
    
