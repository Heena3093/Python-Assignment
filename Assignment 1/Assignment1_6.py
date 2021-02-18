#6.Write a program which accept number from user and check whether that number is positive or negative or zero.
#Input : 11 Output : Positive Number
#Input : -8 Output : Negative Number
#Input : 0 Output : Zero


def ChkNum(value):
    if value> 0:
        return True
    else:
        return False

def main():
    print ("Enter number ")
    no=int(input())

    ret=ChkNum(no)

    if no>0:
        print("Postive Number")
    elif no<0:
        print("Negative Number")
    else:
        print("Number is Zero")

if __name__=="__main__":
    main()