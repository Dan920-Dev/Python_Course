# Convert colones to dollars

"""
The colón has been a monetary unit of El Salvador since 1892. 
It was progressively replaced by the US dollar in 2001. 
The colón was issued since 1934 by the Central Reserve Bank of El Salvador
"""

print("Enter the amount in colones you want to convert to dollars: ")
convertColon = float(input())

result = convertColon / 8.75

print(convertColon, " Colones in dollars is: ", result)