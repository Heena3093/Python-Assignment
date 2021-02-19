#2. Write a program which accept one number and display below pattern.
#Input : 5   Output :* * * * *
#                    * * * * *
#                    * * * * *
#                    * * * * *
#                    * * * * *


def DisplayP(value):

    for i in range(0,value):
        print("\r")
        for j in range(0,value):
            print("*",end=" ")          
            
def main():
    print("Enter number to print pattern")
    no=int(input())
    DisplayP(no)


if __name__=="__main__":
    main()
