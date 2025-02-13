"""
This module is use to make the observer pattern.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>

This file is part of Proyecto1.
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    """This class is used to define the observer."""
    @abstractmethod
    def update(self, message: str):
        """This method is used to update the observer."""
        pass