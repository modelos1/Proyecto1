"""
This file is used to represent the command abstract class.

author: Julian David Pulido Carreño  <judpulidoc@udistrital.edu.co>

This file is part of Proyecto1.


"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod


class Command(ABC):
    """This class is used to represent the command abstract class."""

    @abstractmethod
    def execute(self):
        """This method is used to execute the command."""
