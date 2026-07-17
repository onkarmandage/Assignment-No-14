Even=lambda No1: No1 %5==0

def main():
    Value=int(input("Enter the number "))
    Ret=Even(Value)
    if Ret==True:
        print(True)
      
if __name__=="__main__":
    main()
    