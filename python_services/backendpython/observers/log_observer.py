"""
This module is use to write the log observer for transactions.

author: Julian David Pulido Carreño  <judpulidoc@uditrital.edu.co>

This file is part of Proyecto1.
"""
import os
from observers.observer import Observer

class LogObserver(Observer):
    """This class is used to define the log observer."""
    def update(self, transaction_data: dict):
        """This method is used to update the observer."""
        log_dir = "logs"
        log_file_path = os.path.join(log_dir, "transaction_logs.txt")

        with open(log_file_path, 'a', encoding='utf-8') as file:
            file.write(f"Transaction: {transaction_data}\n")
            file.close()
        print(f"Log registered: {transaction_data}")