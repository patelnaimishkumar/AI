squres=[i**2 for i in range (10)]

print(squres)


x=[(i,i**2) for i in range (10) if i>5]

print(x)

#nested list
m1=[[1, 2, 3, 4],[5,6,7,8],[9,10,11,12]]


c=[]
for i in range(4):
    r    = []
    for x in m1:
        r.append(x[i])
    c.append(r)


print(c)

t=[[x[i] for x in m1] for i in range(4)]

print(t)