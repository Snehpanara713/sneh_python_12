rno=int(input("Enter Roll No:"))
sname=input("Enter Name Of Student:")
s1=int(input("Enter Marks Of Subject 1:"))
s2=int(input("Enter Marks Of Subject 2:"))
s3=int(input("Enter Marks Of Subject 3:"))

total=s1+s2+s3
per=total/3

print("Student Name : ",sname)
print("Roll No : ",rno)
print("Total : ",total)
print("Percentage : ",per)

if per>=70:
    print("Disticntion")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")
