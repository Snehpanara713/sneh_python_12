t=(1,2,1.1,2.2,"tops",True,[100,200,300],10,1,False,"python")

print(t)
print(t.count(0))
print(t.index(True,6))
print(len(t))

for i in t:
    print(i,end=" ")
print()
print(t[6])
t[6].append(400)
print(t)

print(100 in t)
