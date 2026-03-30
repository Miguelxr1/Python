from random import randint

ns = []

for c in range(5):
    ns.append(randint(1, 10))

ns = tuple(ns)

print(f"Os número sorteados foram {ns}")
print(f"O maior número foi {max(ns)}")
print(f"O menor número foi {min(ns)}")
