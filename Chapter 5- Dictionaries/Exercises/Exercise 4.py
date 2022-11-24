rivers = {
    "Nile":"Egypt",
    "Volga":"Russia",
    "Ganges":"India",
}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

for river in rivers.keys():
    print(river.title()) 

for country in rivers.values():
    print(country.title())