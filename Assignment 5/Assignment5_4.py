#4.Write a recursive program which accept number from user and return summation of its digits.
#Input : 879 Output : 24

def SumOfDigit(no):
    
    if no == 0: 
        return 0
    return (no % 10 + SumOfDigit(int(no / 10))) 

def main():
    print("Enter the number:")
    val=int(input())

    ret=SumOfDigit(val)

    print("Sum of digit is {}:".format(ret))

if __name__=="__main__":
    main()

