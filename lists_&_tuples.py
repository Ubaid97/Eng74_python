# Lists are mutable
# We can add, remove, change items in a list

# Creating a list
shopping_list = ["apples", "milk", "bread"]
print(shopping_list)
print(type(shopping_list))

# Indexing
print(shopping_list[1]) # prints out second item: milk
print(shopping_list[1:]) # prints out all items starting from second item
print(shopping_list[-1]) # prints out last item

# Add items
shopping_list.append("eggs") # Append method adds item at the end of the list
print(shopping_list)

# Remove items
shopping_list.remove("apples")
print(shopping_list)

shopping_list.pop() # Removes last item of the list
print(shopping_list)

# Replacing items
shopping_list[1] = "juice" # replaces item at index 1
print(shopping_list)
