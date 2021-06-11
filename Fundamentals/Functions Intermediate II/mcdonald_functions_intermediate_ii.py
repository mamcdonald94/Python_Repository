# 1. Update Values in Dictionaries and Lists

# Change the value 10 in x to 15.
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30


x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30


# 2. Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, given a list of
# dictionaries, the function loops through each dictionary in the list
# and prints each key and the associated value.


def iterateDictionary(some_list):
    for some_dict in some_list:
        for key, value in some_dict.items():
            print(key, value)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


iterateDictionary(students)


# 3. Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, given a
# list of dictionaries and a key name, the function prints the value
# stored in that key for each dictionary.


def iterateDictionary2(key_name, some_list):
    for some_dict in some_list:
        print(some_dict[key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values
# are all lists, prints the name of each key along with the size of its list,
# and then prints the associated values within each key's list.

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key, some_value in some_dict.items():
        print(key, len(some_value))
        for city in some_value:
            print(city)


print(printInfo(dojo))
