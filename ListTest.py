l1=[]
l1.append(1)
l1.append(3)
l1.append("aa")
print(l1)
print(len(l1))
l2=["a","b"]
l1.append(l2)
print(l1)
print(l1.remove(1))
print(l1)
print(l1.extend(l2))

print(l1)

del l1[0]
print(l1.count("a"))

