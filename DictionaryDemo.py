d={11:"Om",27:"Ravi",93:"Darpil",49:"Arth",56:"Shikha",86:"Mansi",47:"Kaumil",89:"Neha"}

print(d)
print(d[93])
print(d.get(5))
print(d.items())
print(d.keys())
print(d.pop(49))
print(d)
print(d.popitem())
print(d)
d1={49:"Arth",89:"Neha"}
d.update(d1)
print(d)
print(d.values())

d[28]="Jigar"
print(d)

for i in d:
    print(i," : ",d[i])
