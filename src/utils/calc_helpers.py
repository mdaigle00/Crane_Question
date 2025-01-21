from typing import Tuple
import numpy as np #Numpy for efficient vecotr and matric operations
import math
from .util import calculate_distance_between_float

#Function to calculate the unit vector
def calculate_unit_vector_float(
    node_i_x: float,
    node_i_y: float,
    node_i_z: float,
    node_j_x: float,
    node_j_y: float,
    node_j_z: float,
) -> Tuple[float, float, float]:
    
    """
    Calculate the unit vector that points from the start location to the end location.

    Args:
        node_i_x: The x component of the starting location.
        node_i_y: The y component of the starting location.
        node_i_z: The z component of the starting location.
        node_j_x: The x component of the ending location.
        node_j_y: The y component of the ending location.
        node_j_z: The z component of the ending location.

    Returns:
        The unit vector from the start location to the end location.
    """
    #Calculates the distance between the two points.
    distance = calculate_distance_between_float(
        node_i_x,
        node_i_y,
        node_i_z,
        node_j_x,
        node_j_y,
        node_j_z,
    )

    #Calculate the vector components.
    i = (node_j_x - node_i_x) / distance
    j = (node_j_y - node_i_y) / distance
    k = (node_j_z - node_i_z) / distance

    return i, j, k #Return unit vector as a tuple


def calculate_moment_about_arbitrary_axis(
    axis_uv: Tuple[float, float, float],
    radius_vector: Tuple[float, float, float],
    force_vector: Tuple[float, float, float],
) -> float:
    """
    Calculates the moment about an arbitrary axis.

    Args:
        axis_uv: The unit vector of the arbitrary axis as a tuple.
        radius_vector: The distance from the arbitrary axis to the force vector as a tuple.
        force_vector: The force vector as a tuple.
    """
    #Convert tupls to numpy arrays for vector operations.
    axis_uv_np = np.array(axis_uv)
    radius_vector_np = np.array(radius_vector)
    force_vector_np = np.array(force_vector)

    #Calculate the overall moment vector using the cross product.
    overall_moment = np.cross(radius_vector_np, force_vector_np)
    
    #Project the momeny vector onto the axis using the dot product
    return float(np.dot(axis_uv_np, overall_moment))

#FFunction to calculate the countering force required to balance a moment.
def calculate_the_countering_force_to_a_moment(
    axis_uv: Tuple[float, float, float],
    moment_about_axis: float,
    suspension_uv: Tuple[float, float, float],
    radius_vector: Tuple[float, float, float],
) -> float:
    """
    Calculates the counteracting force applied by a suspension element  based on the moment about an arbitrary axis.

    Args:
        axis_uv: The unit vector of the arbitrary axis that the moment is about as a tuple.
        moment_about_axis: The moment about the above axis:
        suspension_uv: The unit vector of the suspension that the force acts in.
        radius_vector: The distance from the arbitrary axis to the force vector as a tuple.

    """
    #Calculate the countering force using the given formula.
    return moment_about_axis / (
        (-suspension_uv[1] * radius_vector[2] + suspension_uv[2] * radius_vector[1])
        * axis_uv[0]
        + (suspension_uv[0] * radius_vector[2] - suspension_uv[2] * radius_vector[0])
        * axis_uv[1]
        + (-suspension_uv[0] * radius_vector[1] + suspension_uv[1] * radius_vector[0])
        * axis_uv[2]
    )

#Function to calculate the minimum standoff point for a boom relative to a building
def calculate_minimum_stand_off_point(
    boom_foot_pin_x: float,
    boom_foot_pin_y: float,
    boom_half_width: float,
    building_top_corner_x: float,
    building_top_corner_y: float,
    
):
    #Calculate the distance from the boom's base to the building's top corner.
    boom_foot_pin_to_point_of_impact = math.sqrt(
        (building_top_corner_x - boom_foot_pin_x) ** 2
        + (building_top_corner_y - boom_foot_pin_y) ** 2
    )

    #Calculate the angle from the point of impact to the horizontal. 
    point_of_impact_to_horizontal_angle = math.atan(
        (building_top_corner_y - boom_foot_pin_y)
        / (building_top_corner_x - boom_foot_pin_x)
    )

    #Calculate the angle from the boom's centerline to the point of impact.
    centerline_of_boom_to_point_of_impact_angle = math.atan(
        boom_half_width / boom_foot_pin_to_point_of_impact
    )

    #Calculate the overall angle from the boom's centerline to the horizontal
    centerline_of_boom_to_horizontal_angle = (
        point_of_impact_to_horizontal_angle + centerline_of_boom_to_point_of_impact_angle
    )

    #Calculate the length along the boom to the point of impact.
    impact_length_down_boom = math.sqrt(
        boom_foot_pin_to_point_of_impact ** 2 + boom_half_width ** 2
    )

    #Calculate the x and y offsets for the standoff point.
    standoff_offset_x = impact_length_down_boom * math.cos(
        centerline_of_boom_to_horizontal_angle
    )
    standoff_offset_y = impact_length_down_boom * math.sin(
        centerline_of_boom_to_horizontal_angle
    )

    #Returns the adjusted standoff point coordinates.
    return standoff_offset_x + boom_foot_pin_x, standoff_offset_y + boom_foot_pin_y
