prompt = "What is your age?"


while True:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("Your entry fee is free")
    elif age < 13:
        print("Your entry fee is $10.")
    else:
        print("Your entry fee is $15.")