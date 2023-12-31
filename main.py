import math
import random
import time

start_time = time.time()

# Defines the middle point of the circle
middleLatitude = 37.7749
middleLongitude = -122.4194

# Defines the radius of the circle in miles
radius = 100

# Defines the number of random points to generate
randomPoints = 100000000

# Generates random points within the circle
points = []
for i in range(randomPoints):
    # Generates a random angle and distance from the center point
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(0, radius)

    # Computes the latitude and longitude coordinates of the point
    pointLatitude = middleLatitude + (distance / 111.0) * math.cos(angle)
    pointLongitude = middleLongitude + (distance / (111.0 * math.cos(middleLatitude))) * math.sin(angle)

    # Adds the point to the list of points
    points.append((pointLatitude, pointLongitude))

# Prints the generated points
print(points)

end_time = time.time()
time_taken = end_time - start_time

print("Time taken: {:.2f} seconds ".format(time_taken))