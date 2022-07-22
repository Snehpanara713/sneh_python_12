def MaxOfTwo(a,b):
    if a>b:
        print(a," Is Greater")
    else:
        print(b," Is Greater")

def MaxOfThree(a,b,c):
    if a>b:
        if a>c:
            print(a," Is Greater")
        else:
            print(c," Is Greater")
    elif b>c:
        print(b," Is Greater")
    else:
        print(c," Is Greater")

def Prime(x):
    if x%2!=0:
        for i in range(3,int(x/2)+1,2):
            if x%i==0:
                print(x," Is Not Prime")
                break
        else:
            print(x," Is Prime")
    else:
        print(x," Is Not Prime")

def Fibonaci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()

        
