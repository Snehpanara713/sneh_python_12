'''
Function : It is set of instruction that perform a specific task.
1. Library
2. User Defined
'''
#Function With No Argument & No Return Value

def printLine():
    print("*"*50)

printLine()
print("Welcome To User Defined Function In Python")
printLine()

#Function With Argument But No Return Value

def add(a,b):
    print("Addition : ",a+b)

printLine()
x=int(input("Enter Value:"))
y=int(input("Enter Value:"))
add(x,y)
printLine()

#Function With Argument & Return Value

def sub(a,b):
    return a-b
printLine()
x=int(input("Enter Value:"))
y=int(input("Enter Value:"))
#ans=sub(x,y)
print("Subtraction  ",sub(x,y))
printLine()

