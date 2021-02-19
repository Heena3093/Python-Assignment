#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accept4

import Arithmatic

def main():
    print("Enter first number")
    no1=int(input())

    print("Enter second number")
    no2=int(input())

    ret1=Arithmatic.Add(no1,no2)
    print("Addition of two number is:",ret1)

    ret2=Arithmatic.Sub(no1,no2)
    print("Substraction of two number is:",ret2)

    ret3=Arithmatic.Mult(no1,no2)
    print("Multiplication of two number is:",ret3)

    ret4=Arithmatic.Div(no1,no2)
    print("Division of two number is:",ret4)

if __name__=="__main__":
    main()

