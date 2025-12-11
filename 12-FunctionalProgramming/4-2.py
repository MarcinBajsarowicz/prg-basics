# Recorded speeds from the camera
speeds = [48, 47, 54, 50, 42, 68, 39, 46]

# Filter the speeds that exceed 50 km/h
exceeded_speeds = list(filter(lambda speed: speed > 50, speeds))

# Print the result
print("Vehicles exceeding the speed limit:", exceeded_speeds)
