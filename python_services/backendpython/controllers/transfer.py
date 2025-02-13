"""
This file is the controller for the transfer services.

author: Julian David Pulido Carreño  <judpulidoc@uditrital.edu.co>

This file is part of Proyecto1.


"""
# pylint: disable=import-error
from fastapi import APIRouter, HTTPException
from services.transfer import TransferService

router = APIRouter()
transfer_service = TransferService()

@router.post("/transfer/{sender}/{receiver}/{amount}")
def transfer(sender:str, receiver:str, amount:float):
    """This method is used to transfer money between accounts."""
    try:
        result = transfer_service.transfer_money(sender, receiver, amount)
        return result
    except HTTPException as e:
        raise e
    
@router.put("/deposit/{phone_number}/{amount}")
def deposit(phone_number:str, amount:float):
    """This method is used to deposit money in an account."""
    try:
        result = transfer_service.deposit_money(phone_number, amount)
        return result
    except HTTPException as e:
        raise e

@router.put("/withdraw/{phone_number}/{amount}")
def withdraw(phone_number:str, amount:float):
    """This method is used to withdraw money from an account."""
    try:
        result = transfer_service.withdraw_money(phone_number, amount)
        return result
    except HTTPException as e:
        raise e

