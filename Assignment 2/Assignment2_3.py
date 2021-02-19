#3. Write a program which accept one number from user and return its factorial.
#Input : 5 Output : 120

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    print("Enter number")
    No=int(input())

    ret=factorial(No)
    print("Factorial of {} is {}".format(No,ret))
if __name__=="__main__":
    main()
