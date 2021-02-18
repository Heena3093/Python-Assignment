#3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
#Input : 11 5 Output : 16


def Add(value1,value2):
    sum = 0
    sum = value1 + value2
    return sum


def main():
    print("Enter first number:")
    no1=int(input())

    print("Enter second number:")
    no2=int(input())

    ret = Add(no1,no2)
    print("Addition of two number is:",ret)


if __name__=="__main__":
    main()