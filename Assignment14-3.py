Max=lambda No1,No2 : No1>No2
        
def main():
    Value1=int(input("Enter the first no "))
    Value2=int(input("enter the second no "))
    Ret=Max(Value1,Value2)
    if Ret==True:
        print(Value1," is maximum")
    else:
        print(Value2," is maximum")

if __name__=="__main__":
    main()
