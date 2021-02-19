#4.Write a program which accept one number form user and return addition of its factors.
#Input : 12 Output : 16 (1+2+3+4+6)

def DisplayFactor(number):
    divisors = [0]
    for i in range(1, number):
        if (number % i)==0:
            print(i)
            divisors.append(i)
    return sum(divisors)
    
def main():
    print("Enter the number")
    num=int(input())

    ret=DisplayFactor(num)
    print("Addition of Factors number is",ret)
if __name__=="__main__":
    main()



