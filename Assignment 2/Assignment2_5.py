#5.Write a program which accept one number for user and check whether number is prime or not.
#Input : 5 Output : It is Prime Number
def ChkPrime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")

    else:
        print(number, "is not a prime number")
    
    

def main():
    print("Enter number")
    No=int(input())

    iret=ChkPrime(No)
   

if __name__=="__main__":    
    main()
