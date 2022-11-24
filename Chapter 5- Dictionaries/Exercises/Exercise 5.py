pets = []
pet = {
    "animal type":"Lion",
    "name":"Jack",
    "owner":"John",
    "food":"meat",
}
pets.append(pet)

pet = {
    "animal type":"Goat",
    "name":"Billy",
    "owner":"Ben",
    "food":"Grass",
}
pets.append(pet)

pet = {
    "animal type":"Cat",
    "name":"Luna",
    "owner":"Charlotte",
    "food":"Meat",
}
pets.append(pet)

for pet in pets:
    print("Here's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))