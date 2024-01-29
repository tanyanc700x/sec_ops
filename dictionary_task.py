people_list = [
    {"name": "Galadriel", "age": 6992},
    {"name": " Fili", "age": 25},
    {"name": "Kili", "age": 25},
    {"name": "Torin", "age": 195},
    {"name": "Legalas", "age": 500},
    {"name": "Bilbo", "age": 128},
    {"name": "Saruman", "age": 2400},
    {"name": "Boromir", "age": 87}
]

# Youngest people search:
min_age = min(person["age"] for person in people_list)
youngest_people = [person["name"] for person in people_list if person["age"] == min_age]
print("The youngest people are:", youngest_people, type(youngest_people))

# Longest name search:
max_name_length = max(len(person["name"]) for person in people_list)
longest_names = [person["name"] for person in people_list if len(person["name"]) == max_name_length]
print("The longest names are:", longest_names, type(longest_names))

average_age = sum(person["age"] for person in people_list) / len(people_list)
average_age_list = [average_age]  # конвертуємо float в список
print("The average age is:", average_age_list, type(average_age_list))