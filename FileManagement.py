file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File Written Successfully")
print("*"*70)

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*"*70)

file=open("tops1.txt","a")
file.write("\nThis file is now appended using append mode.")
file.close()
print("File Appended Successfully")
print("*"*70)

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*"*70)

file=open("tops2.txt","w+")
file.write("This is w+ operation in python file management.")
print(file.tell())
file.seek(10)
print(file.read())
file.close()
print("*"*70)


