#1.Write a program which contains one lambda function which accepts one parameter and return power of two.
#Input : 4 Output : 16
#Input : 8 Output : 64
def main():
    print("Enter the number")
    no1=int(input())
    print("Enter the Power")
    no2=int(input())
    val = lambda no1,no2:no1**no2
    print("Power of 2 is :",val(no1,no2))

if __name__=="__main__":
    main()