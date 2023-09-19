conjunto = set([1, 2, 3, 4, 4, 2, 3])
conjunto = { 1, 2, 3, 4, 4, 2, 3, 5 }

print(conjunto)

# Get Values
numbersNoRepeat = list(conjunto)
print(numbersNoRepeat[1])

# Add values
conjunto.add(6)
conjunto.add(2)
print(conjunto)

# Remove values
conjunto.discard(2)
print(conjunto)

# Union
c1 = {1, 2, 3}
c2 = {3, 4, 5}

union = c1.union(c2)
print(union)

#Intersection
intersection = c1.intersection(c2)
print(intersection)

notIntersection = c1.symmetric_difference(c2)
print(notIntersection)

# Difference
diff = c1.difference(c2)
print(diff)

# SuperSet and Subset 
c3 = {4}
print(c3.issubset(c1))
print(c3.issubset(c2))
print(c2.issuperset(c3))
print(c3.isdisjoint(c2))
print(c1.isdisjoint(c3))
