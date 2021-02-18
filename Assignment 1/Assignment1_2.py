#2. Write a program which contains one function named as ChkNum() which accept one parameter as number. 
# If number is even then it should display “Even number” otherwise display “Odd number” on console.
#Input : 11 Output : Odd Number
#Input : 8 Output : Even Number

def ChkNum(value):
    if value%2==0 :
        return True
    else:
        return False
def main():
    print("Enter number:")
    no = int(input())

    iret=ChkNum(no)
    if no%2==0 :
        print("Even number")
    else:
        print("Odd Number")

if __name__=="__main__":
    main()