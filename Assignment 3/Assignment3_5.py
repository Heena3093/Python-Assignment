#5.Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
#Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module 
#named as MarvellousNum. Name of the function from main python file should be ListPrime().
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#Output : 54 (13 + 5 + 7 +2 + 5)


from MarvellousNum import ChkPrime
    
def ListPrime(arr):
    brr = []
    for i in range(len(arr)):
        if ChkPrime(arr[i])==True:
            brr.append(arr[i])
    return brr

def SumPrime(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum

def main():
    arr=[]
    print("Enter the number of elements:")
    size=int(input())
    for i in range(size):
        print("The elemnts are :",i+1)
        no=int(input())
        arr.append(no)
    print("Display the Elements are:",arr)

    ret=ListPrime(arr)
    print("Prime Numbers are:",ret)

    ret1=SumPrime(ret)
    print("Addition of Prime Numbers are:",ret1)

if __name__=="__main__":
    main()