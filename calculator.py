def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def mul(x,y):
    return x*y

x=float(input("enter a number"))
y=float(input("enter a number"))

print("selct operation")
print("1.add")
print("2.sub")
print("3.div")
print("4.mul")

while True:
    choice=input("enter a choice(1/2/3/4): ")
    if choice =='1':
        print(x, "+", y, "=", add(x,y))
    else:
        if choice =='2':
            print(x,"-",y,"=",sub(x,y))
        else:
            if choice=='3':
                print(x,"/",y,"=",div(x,y))
            else:
                if choice=='4':
                    print(x,"*",y,"=",mul(x,y))
                    break
                else:
                    print("this is not valid operator")
    
        


