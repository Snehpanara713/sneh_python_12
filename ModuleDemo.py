import UDF

while True:

    print("*"*50)
    print("1. MaxOfTwo")
    print("2. MaxOfThree")
    print("3. Prime")
    print("4. Fibonaci")
    print("5. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        x=int(input("Enter Value : "))
        y=int(input("Enter Value : "))
        UDF.MaxOfTwo(x,y)
        print("*"*50)
    elif choice==2:
        x=int(input("Enter Value : "))
        y=int(input("Enter Value : "))
        z=int(input("Enter Value : "))
        UDF.MaxOfThree(x,y,z)
        print("*"*50)
    elif choice==3:
        y=int(input("Enter Value : "))
        UDF.Prime(y)
        print("*"*50)
    elif choice==4:
        y=int(input("Enter Value : "))
        UDF.Fibonaci(y)
        print("*"*50)
    else:
        break
