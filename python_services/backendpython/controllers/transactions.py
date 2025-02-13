"""
This module is used to handle services related to transactions.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>
"""
#pylint: disable=import-error
from typing import List
from datetime import datetime
from fastapi import APIRouter, HTTPException
from services.transactions import TransactionsService
from repositories.transactions import TransactionsDAO

router = APIRouter()

services = TransactionsService()


@router.get("/transactions/all")
def get_all_transactions():
    """This method is used to get all transactions.

    Returns:
        List[TransactionsDAO]: A list of transactions.
    """
    return services.get_transactions()


@router.get("/transactions/by_owner/{owner}")
def get_transaction_by_owner(owner:str) -> list[TransactionsDAO]:
    """This method is used to get a transaction by number phone.

    Args:
        owner (str): The number phone of the owner.

    Returns:
        List[TransactionsDAO]: A list of transactions.
    """
    return services.get_transaction_by_owner(owner)


@router.get("/transactions/by_type/{transaction_type}")
def get_transactions_by_type(transaction_type: str) -> List[TransactionsDAO]:
    """This method is used to get transactions by type.

    Args:
        transaction_type (str): The type of the transaction.

    Returns:
        List[TransactionsDAO]: A list of transactions.
    """
    return services.get_transactions_by_type(transaction_type)


@router.get("/transactions/by_date/{transaction_date_start}/{transaction_date_end}")
def get_transactions_by_date(
    transaction_date_start: datetime, transaction_date_end: datetime
) -> List[TransactionsDAO]:
    """This method is used to get transactions by date.

    Args:
        transaction_date_start (str): The start date of the transaction.
        transaction_date_end (str): The end date of the transaction.

    Returns:
        List[TransactionsDAO]: A list of transactions.
    """ 
    if transaction_date_start.date > transaction_date_end.date:
        raise HTTPException(
            status_code=400,
            detail="The start date must be less than the end date.",
        )
    return services.get_transactions_by_date(
        transaction_date_start, transaction_date_end
    )
