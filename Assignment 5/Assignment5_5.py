#5. Write a recursive program which accept number from user and return its factorial.
#Input : 5   Output : 120



def fact(no):
    if(no == 0):
        return 1
    return no * fact(no-1)

def main():
    print("Enter the number:")
    val=int(input())
    ret=fact(val)
    print("factorial number is {} ".format(ret))
if __name__=="__main__":
    main()