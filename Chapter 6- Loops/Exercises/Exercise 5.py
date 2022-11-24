sandwich_orders = ["Chicken sandwich", "Egg sandwich", "Seafood sandwich", "Nutella sandwich", "Tuna sandwich", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = [] 

print("Deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")