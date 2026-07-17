Min=lambda No1,No2:No1>No2

def main():
    Value1=int(input("Enter the first Number "))
    Value2=int(input("Enter the Second Number "))
    Ret=Min(Value1,Value2)
    if Ret==True:
        print(Value2,"is minimum ")
    else:
        print(Value1,"is minimum ")

if __name__=="__main__":
    main()