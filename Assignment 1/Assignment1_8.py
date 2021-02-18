#8. Write a program which accept number from user and print that number of “*” on screen.
#Input : 5 Output : * * * * *

def Display(no):
    for i in range(no):
        print("*",end=" ")

def main():
    print("Enter number to print message")
    value=int(input())

    Display(value)


if __name__=="__main__":
    main()