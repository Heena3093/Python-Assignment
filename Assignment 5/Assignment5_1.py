#1. Write a recursive program which display below pattern.
#Input : 5
#Output : * * * * *

def DisplayP(no):
    if no != 0:
        no = no - 1
        print("*",end=" ")
        DisplayP(no)  # Recursive call 
def main():
    value=5
    DisplayP(value)

if __name__=="__main__":
    main()