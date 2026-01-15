# 01/13: Module 1 Review
# create a list

numbers = [] # creates an empty list
numbers = [15, 23.5, '15', 15] # 0 index, can have different data types, can have duplicates
          #0   1      2    3
print(numbers[1]) # give me element in index 1
print(numbers[1:]) # list slicing, extracts everything
print(numbers[1:3]) # list slicing, extracts index 1 and 2, but not 3
print(numbers[:3]) # list slicing, extracts index 0, 1, and 2, but not 3
print(numbers[-1]) # gives me the last element in the list
print(numbers[-3:]) # list slicing, extracts index -3, -2, and -1, but not 0

print(numbers) # prints the whole list
numbers[2]=100
print(numbers) # prints the whole list with the change

# Methods
numbers.append(120) # adds 120 to the end of the list
print(numbers) # prints the whole list with the change

numbers.extend([25.5, 18]) # adds 25.5 and 18 to the end of the list
print(numbers) # prints the whole list with the change

numbers.insert(3, 30) # adds 30 to index 3, and shifts the rest of the elements to the right
print(numbers) # prints the whole list with the change

numbers.pop() # removes the last element in the list
print(numbers) # prints the whole list with the change

numbers.pop(2) # removes the element in index 2, and shifts the rest of the elements to the left
print(numbers) # prints the whole list with the change

numbers.remove(15) # removes the first occurrence of 15 in the list
print(numbers) # prints the whole list with the change

for num in numbers: # for loop to iterate through the list
    # look for 15
    if num == 15:
        numbers.remove(15)
print(numbers) # prints the whole list with the change

# Comprehension

# Tabular way to create a list
# faster way to create a list
numbers = [15, 23.5, '15', 15]

#define header row before the loop
print(f"{'Index':<10}{'Num'}") # header row with index and num, left aligned with 10 spaces for index
print("-" * 20) # prints a separator line 20 characters long

for num in numbers: # num represents each element in the list
    print(f"{numbers.index(num):<10}{num}") # prints the index and num, left aligned with 10 spaces for index

# Squares of the numbers in the list

numbers = [15, 23.5, 100, 15]
squares = [num**2 for num in numbers] # creates a new list called squares, where each element is the square of the corresponding element in numbers

print(f"{'Index':<10}{'Num':<6} {'Square':<6}") # header row with index, num, and square, left aligned with 10 spaces for index, 6 spaces for num and square
print("-" * 22) # prints a separator line 20 characters long

for num in numbers: # num represents each element in the list
    # get index position
    index = numbers.index(num) # get the index of the current num
    print(f"{index:<10}{num:<6}{squares[index]}") # prints the index, num, and square, left aligned with 10 spaces for index, 6 spaces for num and square

# second 15 is index 0, need to fix it
numbers = [15, 23.5, 100, 15]
squares = [num**2 for num in numbers] # creates a new list called squares, where each element is the square of the corresponding element in numbers

print(f"{'Index':<10}{'Num':<6} {'Square':<6}") # header row with index, num, and square, left aligned with 10 spaces for index, 6 spaces for num and square
print("-" * 22) # prints a separator line 20 characters long

for i, v in enumerate(numbers): # num represents each element in the list, index represents the index of each element
    print(f"{i:<10}{v:<6}{squares[i]}") # prints the index, num, and square, left aligned with 10 spaces for index, 6 spaces for num and square

# enumerate() function returns both the index and value 
