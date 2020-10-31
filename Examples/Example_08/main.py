# List operators or methods

listNumbers = [5, 9, 1, 58, 4, 2.65, 10.8]
print(listNumbers) # We show the list

listNumbers.sort() # Sort the list in ascending order
print(listNumbers) # # We show the list 

# We obtain and display the minimum value of the list
minNumber = min(listNumbers) 
print(minNumber)

# We obtain and display the maximum value of the list
maxNumber = max(listNumbers)
print(maxNumber)

# We obtain and display the number of elements in the list
lengthList = len(listNumbers)
print(lengthList)

# We look for an element in the list and show if it is true or false
searchItem = 5 in listNumbers
print(searchItem)

# Returns the index where the value 4 is in the list
indexLista = listNumbers.index(4)
print(indexLista)

# We look for how many times an element is in the list and we show it
countElement = listNumbers.count(58)
print(countElement)