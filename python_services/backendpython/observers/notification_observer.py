"""
This file simulates the sending of notifications.

author: Julian David Pulido Carreño  <

This file is part of Proyecto1.
"""
from observers.observer import Observer

class NotificationObserver(Observer):
    """Observer used to send notifications."""
    def update(self, transaction_data: dict):
        """This method is used to update the observer."""
        print(f"Notification sent: {transaction_data}")
        