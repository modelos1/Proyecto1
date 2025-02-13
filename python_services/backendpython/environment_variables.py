"""
This module has a class to handle the environment variables into the application.

author: Julian David Pulido Carreño  <judpulidoc@usitrital.edu.co>


"""
import os
from dotenv import load_dotenv

load_dotenv()

# pylint: disable=too-few-public-methods
class EnvironmentVariables:
    """
    This class has the methods to handle the environment variables into the application.

    """

    def __init__(self):
        """
        This method is used to initialize the class (constructor).

        """
        self.path_transactions_data = os.getenv("PATH_TRANSACTIONS_DATA")
        self.path_account_data = os.getenv("PATH_ACCOUNTS_DATA")
