# Dictionaries store data in key:value pairs
# can store any type of data

students_data = {"key": "value",
                 "name": "Ubaid",
                 "stream": "tech",
                 "completed lessons": 4,
                 "lesson names": ["variables", "operators", "data types", "lists"]
                 }

# get a particular value by calling its key
print(students_data["name"])
print(students_data["lesson names"][2])

# .key() - returns all keys in the dictionary
# .values() - returns all values