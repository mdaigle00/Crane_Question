import sys
from .utils.calcs import calculate_load_displacement_above_building, calculate_main_hoist_tension
from .models.crane import Crane

def main():
    # Create the input parameters
    # Crane base position in global coordinates (Feet)
    boom_foot_pin_x = 6.458333333333333  # 6ft 5.5in
    boom_foot_pin_y = 9.9375  # 9ft 11.25in

    # Boom characteristics
    boom_length = 100.0  # 100ft
    boom_width = 2.8333333333333335  # 2ft 10in

    # Main suspension connection point on the boom
    main_suspension_point_x = 20.6875  # 20ft 8.25in
    main_suspension_point_y = 10.416666666666666  # 10ft 5in

    # Building dimensions
    building_height = 50.0  # 50ft
    distance_from_building = 10.0  # 10ft

    # Load that will be lifted
    hook_load = 50000  # lbf

    # Create the crane object
    crane = Crane(
        base_position=(boom_foot_pin_x, boom_foot_pin_y),
        boom_length=boom_length,
        boom_angle=45.0,  # Example angle
        hoist_start=(main_suspension_point_x, main_suspension_point_y, building_height),
        hoist_end=(boom_length, 0.0, building_height),  # Example hoist end point
    )

    # Calculate maximum load displacement
    A = distance_from_building
    B = calculate_load_displacement_above_building(crane, A, building_height)

    if B and len(B) == 2:
        print(f'Maximum Load Displacement Above Building: x={B[0]:.2f} ft, y={B[1]:.2f} ft')
    else:
        print("Error: Unable to calculate load displacement above the building.")

    # Calculate main hoist tension
    tension = calculate_main_hoist_tension(crane, hook_load)
    print(f'Main Hoist Tension: {tension:.2f} lbf')

if __name__ == "__main__":
    main()
