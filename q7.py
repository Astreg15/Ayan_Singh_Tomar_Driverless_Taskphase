print("--- Set the Reference Point ---")
ref_x = float(input("Enter reference X: "))
ref_y = float(input("Enter reference Y: "))
def calculate_distance(point):
    x = point[0]
    y = point[1]
    distance = (x-ref_x)**2 + (y-ref_y)**2
    return distance
print("\n--- Enter the Coordinates to Sort ---")
num_points = int(input("How many points do you want to enter? "))
coordinates = []
for i in range(num_points):
    print(f"\nPoint {i+1}:")
    point_x = float(input("  Enter X coordinate: "))
    point_y = float(input("  Enter Y coordinate: "))
    new_point = (point_x, point_y)
    coordinates.append(new_point)
coordinates.sort(key=calculate_distance)
print("\n--- Sorted Coordinates ---")
print(f"Points sorted by proximity to ({ref_x}, {ref_y}):")
print(coordinates)