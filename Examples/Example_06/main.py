# Lists

"""
A list is a data structure and data type in python with special characteristics. 
The special thing about lists in Python is that they allow us to store any type of value such as integers, 
strings and even other functions
"""

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
print(days) # Show list day

day = days[0] # An index is an integer that indicates the position of an item in a list. 
              # The first item in a list always starts at index 0 and Show Monday  
print(day)

day = days[5]
print(day) # Show Saturday
# if day we equate it to an index greater than 6 we will have an error

# Cycle the list in reverse
day = days[-1] # -1 refers to the last index in the list and Show Sunday 
print(day)

day = days[-5]
print(day) # Show Wednesday