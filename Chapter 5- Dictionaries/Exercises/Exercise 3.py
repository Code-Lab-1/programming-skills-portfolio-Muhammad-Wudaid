glossary = {
    "Lists":"Lists are used to store multiple items in a single variable.",
    "Variables":"Variables are containers for storing data values.",
    "String":"In Python, strings are collections of bytes that represent Unicode characters.",
    "Loops":"Loops allow us to repeatedly run a set of commands.",
    "Dictionaries":"Dictionaries are used to keep data values in key:value pairs.",
    "Tuples":"Tuples are used to hold many items in a single variable.",
    "Booleans":"Booleans only have two possible values: True or False.",
    "Fuctions":"A function is a piece of code that only executes when called.",
    "Operators":"Operators are used to execute operations on variables and values.",
    "Arrays":"Arrays are used to hold several values in a single variable.",
}

for items, definiton in glossary.items():
    print("\n" + items.title() + ": " + definiton)