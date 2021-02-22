#Write a program which contains one lambda function which accepts two parameters and return its multiplication.
#Input : 4 3 Output : 12
#Input : 6 3 Output : 18

def main():
    print("Enter the number")
    x=int(input())
    print("Enter the Power")
    y=int(input())
    val = lambda x,y:x*y
    print("Multiplication of 2 number is :",val(x,y))

if __name__=="__main__":
    main()