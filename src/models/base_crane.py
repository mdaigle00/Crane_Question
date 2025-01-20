import math
from typing import Tuple
import numpy as np

#Deine the BaseCrane class.

class BaseCrane:
    def __init__(self, position: Tuple[float, float]) -> None:
        """
        Initialize the base crane.

        Args:
            position (Tuple[float, float]): The (x, y) position of the crane base.
        """
        #Stores the crane's base position as a tuple of (x,y) coordinates.
        self.position = position
