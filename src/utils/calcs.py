from ..utils.calc_helpers import (
    calculate_minimum_stand_off_point,
    calculate_moment_about_arbitrary_axis,
    calculate_the_countering_force_to_a_moment,
)

#Funtion to calculate the maximum load displacement above the building.
def calculate_load_displacement_above_building(crane, distance_from_building, building_height):
    # Extract necessary parameters from the Crane object
    boom_foot_pin_x = crane.base_crane.position[0]
    boom_foot_pin_y = crane.base_crane.position[1]
    boom_half_width = crane.boom.length / 2  # Assume half the boom length as width
    building_top_corner_x = distance_from_building
    building_top_corner_y = building_height

    # Calculate the minimum standoff point using a helper function
    stand_off = calculate_minimum_stand_off_point(
        boom_foot_pin_x,
        boom_foot_pin_y,
        boom_half_width,
        building_top_corner_x,
        building_top_corner_y,
    )
    #Return the calculated standoff position
    return stand_off

#Function to calculate the tension on the main hoist.
def calculate_main_hoist_tension(crane, hook_load):

    #Calculate the end position of the boom
    boom_end = crane.calculate_boom_end_position()
    
    #Calculate the moment about the z-axis
    moment = calculate_moment_about_arbitrary_axis(
        (0, 0, 1),  # Arbitrary axis (z-axis in this case, as it’s 2D)
        (
            boom_end[0] - crane.base_crane.position[0],
            boom_end[1] - crane.base_crane.position[1],
            0,
        ),  # Radius vector
        (0, -hook_load, 0),  # Hook load force vector
    )

    #Calculate the counteracting force required to balance the moment
    return calculate_the_countering_force_to_a_moment(
        (0, 0, 1),  # Axis of rotation
        moment,
        crane.get_main_hoist_unit_vector(),
        (
            boom_end[0] - crane.main_hoist.start_location[0],
            boom_end[1] - crane.main_hoist.start_location[1],
            0,
        ),
    )
