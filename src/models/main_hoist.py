from typing import Tuple
import numpy as np

# MainHoist class
class MainHoist:
    def __init__(self, start_location: Tuple[float, float, float], end_location: Tuple[float, float, float]) -> None:
        """
        Initialize the Main Hoist object with start and end locations while calculating the unit vector.

        Args:
            start_location (Tuple[float, float, float]): The starting position of the hoist (x, y, z).
            end_location (Tuple[float, float, float]): The ending position of the hoist (x, y, z).
        """
        self.start_location = start_location
        self.end_location = end_location
        self.unit_vector = self.calculate_unit_vector()

    def calculate_unit_vector(self) -> Tuple[float, float, float]:
        """
        Calculate the unit vector from the start to the end location.

        Returns:
            Tuple[float, float, float]: The unit vector.
        """
        distance = np.sqrt(
            (self.end_location[0] - self.start_location[0]) ** 2
            + (self.end_location[1] - self.start_location[1]) ** 2
            + (self.end_location[2] - self.start_location[2]) ** 2
        )
        return (
            (self.end_location[0] - self.start_location[0]) / distance,
            (self.end_location[1] - self.start_location[1]) / distance,
            (self.end_location[2] - self.start_location[2]) / distance,
        )
