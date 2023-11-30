# Define sets A, B, C, and D
A = {'a', 'b', 'h', 'j', 'l'}
B = {'b', 'c', 'h', 'l', 'r', 'v'}
C = {'j', 'k', 'n', 't', 'z'}
D = {'b', 'i', 'k', 'v', 'w'}

# Operation X: (A ∪ B) ∩ C
X = (A.union(B)).intersection(C)

# Operation Y: (¬A ∩ ¬B) / (C ∪ D)
universal_set = set(map(str, range(0, 100)))
Y = (universal_set - A.union(B)).intersection(C.union(D))

# Print the results
print(f"X = {X}")
print(f"Y = {Y}")
