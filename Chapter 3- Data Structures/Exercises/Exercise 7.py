list = ['Great Wall of China', 'Taj Mahal', 'Leaning Tower of Pisa', 'Pyramid of Giza', 'Statue of Liberty']
print(list)

print("Alphabetical order:")
print(sorted(list))

print("Original order:")
print(list)

print("Reverse alphabetical order:")
print(sorted(list, reverse=True))

print("Original order:")
print(list)

print("Reversed:")
list.reverse()
print(list)

print("Original order:")
list.reverse()
print(list)

print("Alphabetical order:")
list.sort()
print(list)

print("Reverse alphabetical order:")
list.sort(reverse=True)
print(list)