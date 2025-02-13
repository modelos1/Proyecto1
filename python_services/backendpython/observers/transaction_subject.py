"""
This file administers the observers and notify them when a transaction is made.

author: Julian David Pulido Carreño  <judpulidoc@usitrital.edu.co>

This file is part of Proyecto1.

"""

from observers.observer import Observer


class TransactionSubject:
    """This class is used to define the transaction subject."""

    def __init__(self):
        """This method is used to initialize the class (constructor)."""
        self.observers = []

    def attach(self, observer: Observer):
        """This method is used to attach an observer."""
        self.observers.append(observer)

    def detach(self, observer: Observer):
        """This method is used to detach an observer."""
        self.observers.remove(observer)

    def notify(self, transaction_data: dict):
        """This method is used to notify the observers."""
        for observer in self.observers:
            observer.update(transaction_data)
