fruits = ["maça", "banana", "maracujá", "limão", "laranja"]

print(fruits[-1])
print(fruits[:2])
print(fruits[2:])
print(fruits[:])
print("\n")

# Filter 1
numbers = [1, 30, 21, 2, 9, 65, 34]
pares = []

for num in numbers:
    if num % 2 == 0:
        pares.append(num)

# Filter 2
numbers = [1, 30, 21, 2, 9, 65, 34]
pares = [num for num in numbers if num % 2 == 0]

# Map
double_numbers = [num*2 for num in numbers]

print(pares)
print(double_numbers)
print("\n")

# Add Elements
lista = []

lista.append(1)
lista.append("Maurrici")
lista.append([True, False])
print(lista)
print("\n")

# Remove elements
lista.pop(2) # Remove by index
print(lista)
lista.remove(1) # Remove by value
print(lista)
lista.clear() # Remove all elements
print(lista)
print("\n")

# Count elements
lista = ["python", "js", "js", "html", "js", "html"]

print(len(lista)) # Count all elements of list
print(lista.count("js")) # Count the ocorrences of element
print("\n")

# Find elements
print(lista.index("x")) # Find index of the first occurrence

# Union of list
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]

lista1.extend(lista2)
print(lista1)