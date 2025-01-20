from typing import Tuple
from .base_crane import BaseCrane
from .boom import Boom
from .main_hoist import MainHoist


# Creates the crane class.
class Crane:
    def __init__(
        self,
        base_position: Tuple[float, float],
        boom_length: float,
        boom_angle: float,
        hoist_start: Tuple[float, float, float],
        hoist_end: Tuple[float, float, float],
    ) -> None:
        """
        Initialize the Crane with its components.

        Args:
            base_position (Tuple[float, float]): Position of the base of the crane (x, y).
            boom_length (float): Length of the boom.
            boom_angle (float): Angle of the boom in degrees.
            hoist_start (Tuple[float, float, float]): Starting position of the hoist (x, y, z).
            hoist_end (Tuple[float, float, float]): Ending position of the hoist (x, y, z).
        """
        #Initialize the base of the crane.
        self.base_crane = BaseCrane(position=base_position)
        #Initialize the boom.
        self.boom = Boom(length=boom_length, angle=boom_angle)
        #Initialize the main hoist.
        self.main_hoist = MainHoist(start_location=hoist_start, end_location=hoist_end)

    def calculate_boom_end_position(self) -> Tuple[float, float]:
        """
        Calculate the end position of the boom based on its angle and length.

        Returns:
            Tuple[float, float]: The (x, y) coordinates of the boom's end.
        """
        #Calulcates and returns the boom's end position.
        return self.boom.calculate_end_position(self.base_crane.position)

    def get_main_hoist_unit_vector(self) -> Tuple[float, float, float]:
        """
        Retrieve the unit vector of the main hoist.

        Returns:
            Tuple[float, float, float]: The unit vector of the main hoist.
        """
        #Return the unit vector from the MainHoist class.
        return self.main_hoist.unit_vector

# Calculation Functions
def calculate_load_displacement_above_building(
    crane: Crane, distance_from_building: float, building_height: float
) -> float:
    """
    Calculate the maximum distance from the edge of the building that a load can be placed.

    Args:
        crane (Crane): The crane object.
        distance_from_building (float): Distance from the building edge to the crane base.
        building_height (float): Height of the building.

    Returns:
        float: Maximum distance for load placement.
    """
    #Calculate the minimum standoff point between the crane and building.
    stand_off_x, stand_off_y = calculate_minimum_stand_off_point(
        crane.base_crane.position[0],
        crane.base_crane.position[1],
        0.5 * crane.boom.length,  # Assume half the boom length for width
        distance_from_building,
        building_height,
    )
    #Calcualte the distance from the edge of the building to the standoff point.
    return math.sqrt((stand_off_x - distance_from_building) ** 2 + stand_off_y ** 2)

def calculate_main_hoist_tension(crane: Crane, hook_load: float) -> float:
    """
    Calculate the tension on the main hoist based on the hook load.

    Args:
        crane (Crane): The crane object.
        hook_load (float): The load applied to the hook.

    Returns:
        float: Tension in the main hoist.
    """
    #Calculate the end position of the boom.
    boom_end = crane.calculate_boom_end_position()

    #Calculate the momeny about an arbitrary axis due to the load at the boom's end.
    moment = calculate_moment_about_arbitrary_axis(
        (0, 0, 1),
        (
            boom_end[0] - crane.base_crane.position[0],
            boom_end[1] - crane.base_crane.position[1],
            0,
        ),
        (0, -hook_load, 0),
    )
    #Calculate the countering force required to balance the momeny.
    return calculate_the_countering_force_to_a_moment(
        (0, 0, 1),
        moment,
        crane.get_main_hoist_unit_vector(),
        (
            boom_end[0] - crane.main_hoist.start_location[0],
            boom_end[1] - crane.main_hoist.start_location[1],
            boom_end[2] - crane.main_hoist.start_location[2],
        ),
    )
