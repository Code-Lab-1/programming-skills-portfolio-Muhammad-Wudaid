prompt = "What toppings do you want on your pizza?"
prompt += " \nOnce you're done, type 'quit.'"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(" I'll add " + topping + " to your pizza.")
    else:
        break