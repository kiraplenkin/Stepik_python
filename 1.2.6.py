x = [1, 2, 3]

print(type(x))
print(type(4))

print(type(type(x)))



ans = 0
uniq_objects = []

for obj in objects: # доступная переменная objects
    if obj not in uniq_objects:
        uniq_objects.append(obj)
        ans += 1

print(ans)