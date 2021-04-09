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

# Write the function to add new countries to the travel_log. 👇

def add_new_country(country_visited, num_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = num_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
