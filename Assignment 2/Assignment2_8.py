#8. Write a program which accept one number and display below pattern.
#Input : 5    Output : 1
#                      1 2
#                      1 2 3
#                      1 2 3 4
#                      1 2 3 4 5
#


def DisplayP(num):
    for i in range(1,num+1):
        print("\r")
        for j in range(1,i+1):
            print(j,end=" ")

def main():
    print("Enter the number to print this pattern")
    no=int(input())
    DisplayP(no)
if __name__=="__main__":
    main()