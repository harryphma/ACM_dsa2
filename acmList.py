# Creating a sample list
my_list = [10, 20, 30, 40, 50]

# Using len() to get the length of the list
print("Length of the list:", len(my_list))

# Accessing elements using index - in this case the 3rd element
print("Element at index 2:", my_list[2])

# Slicing the list to get a subset - from index 1 to index 3
print("Sliced list from index 1 to 3:", my_list[1:4])

# Iterating through the list using a for loop
print("Iterating through the list:")
for element in my_list:
    print(element)

# Appending a new element to the list
my_list.append(60)
print("List after appending 60:", my_list)