sandwich_orders = ["Chicken sandwich", "Egg sandwich", "Seafood sandwich", "Nutella sandwich", "Tuna sandwich"]
finished_sandwiches = [] 

for l in sandwich_orders:
    print("I made your " + l)
    finished_sandwiches.append(sandwich_orders)

for sandwich in finished_sandwiches:
    print("Your " + sandwich + " is ready.")