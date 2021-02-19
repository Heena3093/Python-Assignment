#10. Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934 Output : 37


def DisplayDigitAdd(n):
    sum = 0
    while (n != 0): 
        sum = sum + int(n % 10)
        n = int(n/10) 
    return sum
    
def main():
    print("Enter the number")
    num=int(input())

    ret=DisplayDigitAdd(num)
    print("Addition of number is",ret)
if __name__=="__main__":
    main()


