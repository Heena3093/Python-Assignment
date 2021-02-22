#4.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
#List contains the numbers which are accepted from user. 
#Filter should filter out all such numbers which are even. 
#Map function will calculate its square.
#Reduce will return addition of all that numbers.
#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204


def CheckEven(no):
    if no % 2 == 0:
        return True
    else:
        return False

def Filter(arr):
    brr = []
    for i in range(len(arr)):
        if CheckEven(arr[i])==True:
            brr.append(arr[i])
    return brr

def Map(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]*arr[i]
    return arr

def Reduce(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
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

    ret=Filter(arr)
    print("After filtering data is :",ret)

    ret1=Map(ret)
    print("After map data is :",ret1)

    output=Reduce(ret1)
    print("After Reduce data is :",output)

  
if __name__=="__main__":
    main()