'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-12-13 11:47:50
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-12-13 11:49:51
FilePath: \smart_hydroponic_farm\src\lab\torque.py
Description: This is the default setting, please set `customMade`, open koroFileHeader to view the configuration and make settings: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Calculate the required torque
# Given data
load_weight_min = float(input("Enter the minimum load weight (grams): "))
load_weight_max = float(input("Enter the maximum load weight (grams): "))
lever_arm = float(input("Enter the lever arm (centimeters): "))
acceleration = float(input("Enter the acceleration (centimeters per square second): "))

# Convert units to standard units: kilograms (kg) and meters (m)
load_weight_min_kg = load_weight_min / 1000  # convert to kilograms
load_weight_max_kg = load_weight_max / 1000  # convert to kilograms
lever_arm_m = lever_arm / 100  # convert to meters
acceleration_m_s2 = acceleration / 100  # convert to meters per square second

# Acceleration due to gravity
gravity_acceleration = 9.81  # meters per square second (m/s^2)

# Safety factor, usually taken between 1.5 to 2
safety_factor = 1.5

# Torque calculation formula
# Torque = (load weight * lever arm * gravity acceleration) + (load inertia * acceleration)
# Assuming inertia can be neglected, torque is mainly determined by the gravity component
torque_min = load_weight_min_kg * lever_arm_m * gravity_acceleration * safety_factor
torque_max = load_weight_max_kg * lever_arm_m * gravity_acceleration * safety_factor

print("Minimum torque: {:.2f} Nm".format(torque_min))
print("Maximum torque: {:.2f} Nm".format(torque_max))
