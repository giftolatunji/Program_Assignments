us_cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Homphis","Boston", "Los Angeles", "New Orleans"]

fav_anime = ["One Piece", "Bleach", "Fullmetal Alchemist", "Tokyo Ghoul", "The Disastrous Life of Saiki K."]
fav_anime[0] = "YuYu Hakasho"

three_cities = us_cities[0:3]
print(fav_anime)
us_cities[1] = "Orlando"
us_cities.append("New Jersey")
us_cities.extend(["Santa Cruz", "Selma", "Chicago"])
us_cities.insert(7, "Washington, D.C.")

boolean = "One Piece"
print (boolean)

for city in us_cities:
    print(city)