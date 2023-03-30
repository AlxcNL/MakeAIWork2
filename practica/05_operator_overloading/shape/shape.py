import math

from abc import ABC, abstractmethod
from dataclasses import dataclass

# Abstraction: Abstract Superclass
class Shape(ABC):
    # Constructor method with Arguments/Parameters
    def __init__(self, width, height):
        # Self
        # Attributes
        self.width = width
        self.height = height

    # Interface
    @abstractmethod
    # Self
    def area(self, width, height):
        pass

    # Static variable
    pi = math.pi
