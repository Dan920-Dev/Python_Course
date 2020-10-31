# Calculate travel time

"""
The user must enter the distance from their destination and the speed at which they travel, 
the program must calculate the time it will take to reach their destination
"""

print("Enter the distance from your destination in km: ")
distance = float(input())
print("Enter the speed with which you travel in km/h: ")
speed = float(input())

resultTime = distance / speed

print("The time it will take to reach your destination is: ", resultTime, " hours")