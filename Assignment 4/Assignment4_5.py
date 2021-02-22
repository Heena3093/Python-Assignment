#5.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
#List contains the numbers which are accepted from user. 
#Filter should filter out all prime numbers. 
#Map function will multiply each number by 2. 
#Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62


def ChkPrime(no):
    if (no == 1):
        return False
    elif (no == 2):
        return True
    else:
        for i in range(2,no):
            if no % i == 0:
                return False
        return True

def PrimeFilter(arr):
    brr = []
    for i in range(len(arr)):
        if ChkPrime(arr[i])==True:
            brr.append(arr[i])
    return brr

def PrimeMap(arr):
    for i in range(len(arr)):
        arr[i]=arr[i] * 2
    return arr

def PrimeReduce(arr):
    sum = 1
    for i in range(len(arr)):
        sum=arr[i] * 2
    return sum



def main():
    arr=[]
    print("Enter the number of elements:")
    size=int(input())

    for i in range(size):
        print("Enter element number :",i+1)
        no=int(input())
        arr.append(no)    
    print("Your entered data is :",arr)

    ret=PrimeFilter(arr)
    print("After filtering data is :",ret)

    ret1=PrimeMap(ret)
    print("After Map data is :",ret1)

    output=PrimeReduce(ret1)
    print("After Map data is :",output)

if __name__=="__main__":
    main()