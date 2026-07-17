Maximum=lambda a,b,c: a if (a>b and a>c) else ( b if b>a and b>c else c)  

def main():
    No1=int(input("Enter the first number "))
    No2=int(input("Enter the second number "))
    No3=int(input("Enter the third number "))
    Ret=Maximum(No1,No2,No3)
    print("Maximum no is",Ret)
if __name__=="__main__":
    main()