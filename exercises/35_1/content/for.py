restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

min_rating = 3.0

# EQUIVALENTE AO forEach EM JS:
# filtered_restaurants = []

# for restaurant in restaurants:
#     if restaurant["nota"] >= min_rating:
#         filtered_restaurants.append(restaurant)

# EQUIVALENTE AO map + filter EM JS:
filtered_restaurants = [restaurant["name"]  # aqui pedimos somente o nome do
                                            # restaurante
                        for restaurant in restaurants
                        if restaurant["nota"] > min_rating]

print(filtered_restaurants)
