l=[1,2,1.1,2.2,"tops",1,10,"python",100,True,1,False]

print(l)
print(len(l))

l.append(1000)
print(l)

#l.clear()
#print(l)

l1=l.copy()
print(l1)
l1.append(2000)
print(l)
print(l1)

l2=l
print(l2)
l2.append(3000)
print(l)
print(l2)

l3=["C","C++","Java"]
l.extend(l3)
print(l)

print(l.index(10))

l.insert(6,101)
print(l)

l.pop()
print(l)

l.pop(3)
print(l)

l.remove("tops")
print(l)

l.reverse()
print(l)


