travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
#🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(key, key1, key2):
  new_country = {}
  new_country["country"] = key
  new_country["visits"] = key1
  new_country["cities"] = key2
  travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country(key="Russia", key1=2, key2=["Moscow", "Saint Petersburg"])
print(travel_log)
