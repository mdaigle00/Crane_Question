import math
from typing import Tuple

#Define the Boom class.
class Boom:
    def __init__(self, length: float, angle: float) -> None:
        """
        Initialize the boom.

        Args:
            length (float): Length of the boom.
            angle (float): Angle of the boom in degrees.
        """
        #Store the length of the boom.
        self.length = length
        
        #Store the angle of the boom in degrees.
        self.angle = angle

    def calculate_end_position(self, base_position: Tuple[float, float]) -> Tuple[float, float]:
        """
        Calculate the end position of the boom.

        Args:
            base_position (Tuple[float, float]): The (x, y) coordinates of the boom's base.

        Returns:
            Tuple[float, float]: The (x, y) coordinates of the boom's end.
        """

        #Calculate the x-coordinate of the boom's end.
        # Use trig to give the horizontal distance.
        x = base_position[0] + self.length * math.cos(math.radians(self.angle))

        #Calculate the y-coordinate of the boom's end.
        #Use trig to give the vertical distance.
        y = base_position[1] + self.length * math.sin(math.radians(self.angle))
        
        #Return the calculated end position as a tuple (x,y).
        return x, y
