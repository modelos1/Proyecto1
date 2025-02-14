"""
This is the api getway for the project that will be used to manage the requests to the user service and the transaction service.

author: Julian Pulido <judpulidoc@udistrital.edu.co>

this file is part of the project Proyecto1
"""

from fastapi import Depends, FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()

USER_SERVICE_URL = "http://host.docker.internal:8080/v1/users"
TRANSACTION_SERVICE_URL = "http://localhost:8000"

sessions = {}

class AuthDTO(BaseModel):
    """This class is used to validate the auth data"""
    phone_number: str
    password: str

def get_user_authenticated():
    """Retrieve the authenticated user's session"""
    if not sessions:
        raise HTTPException(status_code=401, detail="No users authenticated")
    
    phone_number = list(sessions.keys())[0]  # Get the first phone number
    user_data = sessions[phone_number]

    if not user_data or not isinstance(user_data, dict):
        raise HTTPException(status_code=401, detail="User not authenticated")

    return {**user_data, "phone_number": phone_number} # Return the user data with the phone number

@app.post("/login")
def login(auth_data: AuthDTO):
    """This method is used to login a user redirecting the request to the user service"""
    response = requests.post(
        f"{USER_SERVICE_URL}/login", json=auth_data.dict(), timeout=10)

    if response.status_code == 200:
        user_data = response.json()
        # delete password from user data
        user_data.pop("password", None)
        # Save user data in session
        sessions[auth_data.phone_number] = user_data
        return {
            "message": "User authenticated",
            "session": sessions
        }
    return HTTPException(status_code=response.status_code, detail="Invalid credentials")

@app.get("/account")
def get_account(user: dict = Depends(get_user_authenticated)):
    """This method is used to get the account of the user"""
    response = requests.get(
        f"{TRANSACTION_SERVICE_URL}/account/{user['phone_number']}", timeout=10
    )
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.json())

@app.get("/transactions/all")
def get_transactions_all(user: dict = Depends(get_user_authenticated)):
    """This method is used to get all the transactions of the user"""
    response = requests.get(
        f"{TRANSACTION_SERVICE_URL}/transactions/by_owner/{user['phone_number']}", timeout=10
    )
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.json())

@app.put("/deposit/{amount}")
def deposit(amount: float, user: dict = Depends(get_user_authenticated)):
    """This method is used to deposit money to the user account"""
    response = requests.put(
        f"{TRANSACTION_SERVICE_URL}/deposit/{user['phone_number']}/{amount}", timeout=10
    )
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.json())

@app.put("/withdraw/{amount}")
def withdraw(amount: float, user: dict = Depends(get_user_authenticated)):
    """This method is used to withdraw money from the user account"""
    response = requests.put(
        f"{TRANSACTION_SERVICE_URL}/withdraw/{user['phone_number']}/{amount}", timeout=10
    )
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.json())

@app.post("/transfer/{receiver}/{amount}")
def transfer(receiver: str, amount: float, user: dict = Depends(get_user_authenticated)):
    """This method is used to transfer money to another user"""
    response = requests.post(
        f"{TRANSACTION_SERVICE_URL}/transfer/{user['phone_number']}/{receiver}/{amount}", timeout=10
    )
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.json())
