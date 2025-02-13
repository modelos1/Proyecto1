"""
This is the main module of the project. It is used to run the application.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>
"""

from fastapi import FastAPI

from controllers import transactions_router, accounts_router, transfer_router

app = FastAPI(
    title="Transactions API",
    description="This is an API to handle transactions of a digital wallet.",
    version="0.0.1",
)

app.include_router(transactions_router)
app.include_router(accounts_router)
app.include_router(transfer_router)
