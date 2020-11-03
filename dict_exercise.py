# Creating dictionary containing user details
user_details = {"first name": "John",
                "last name": "Doe",
                "Date of birth": "03/12/1997",
                "age": "22",
                "address": "12 Sesame st",
                "course": "DevOps",
                "grades": "A",
                "hobbies": ["football", "movies", "reading"]
}

print(user_details)
print(type(user_details))

# Added postcode to the dictionary
user_details["postcode"] = "ab1 2cd"
print(user_details)

# Removed grades
user_details.pop("grades")
print(user_details)

# Changed house number from 12 to 13 in the address
user_details["address"] = "13 Sesame st"
print(user_details)

# displayed hobbies list in reverese order
print(user_details["hobbies"][::-1])

# Making changes to hobby list in dictionary
user_details["hobbies"].append("running")
print(user_details["hobbies"])
user_details["hobbies"].remove("movies")
print(user_details["hobbies"])
