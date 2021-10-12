# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = float(random.randint(1, 5))
# print(random_float)
#  Storing states names in as a list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#  Getting Total number of items in a list and storing the value to a variable.
num_of_states = len(states_of_america)
#  total items 50 but index start with 0 so to call the last item we can simply use -1 to the num_of_states integer
#  total len of states is 50 index start with 0 so add -1 to account the last item
print(states_of_america[num_of_states - 1])


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
Vegitables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#  Adds two lists into a list both lists seperated by [ ]
nested_list = [fruits, Vegitables]
