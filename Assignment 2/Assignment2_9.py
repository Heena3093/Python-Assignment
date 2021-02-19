#9. Write a program which accept number from user and return number of digits in that number.
#Input : 5187934 Output : 7

def CountNo(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
    
def main():
    print("Enter the number")
    num=int(input())
    ret=CountNo(num)
    print("The number of {} digit is:{}".format(num,ret))
if __name__=="__main__":
    main()