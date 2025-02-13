"""
This module is use to handle services related to accounts.

author: Julian David Pulido Carreño  <judpulidoc@udisrital.edu.co>

This file is part of Proyecto1.

"""
from fastapi import APIRouter, HTTPException
from repositories.account import ActualAccountDAO
from services.account import AccountService

router = APIRouter()

services = AccountService()

@router.get("/account/{phone_number}")
def get_actual_account(phone_number:str) -> ActualAccountDAO:
    """This method is used to get the actual account.
    Returns:
        ActualAccount: The actual account.
    """
    account = services.get_actual_account(phone_number)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found.")
    return account

@router.put("/account/{phone_number}/{amount}/{type_transaction}")
def update_balance(phone_number:str, amount:float, type_transaction:str):
    """This method is used to update the balance of the account."""
    services.update_balance(phone_number, amount, type_transaction)

