Add=lambda No1,No2: No1+No2

def main():
    Value1=int(input("Enter the first no "))
    Value2=int(input("Enter the second no "))
    Ret=Add(Value1,Value2)
    print("Addition is ",Ret)

if __name__=="__main__":
    main()