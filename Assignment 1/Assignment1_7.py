#7.Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
#Input : 8 Output : False
#Input : 25 Output : True

def DivBy5(value):
    if value % 5 == 0:
        return True
    else:
        return False



def main():
    print ("Enter number ")
    no=int(input())

    ret=DivBy5(no)

    if no % 5 == 0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5 ")

if __name__=="__main__":
    main()