s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))

print({1, 78}.issubset(s1))
print(s2.issuperset({7, 1}))