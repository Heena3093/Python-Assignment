#3.Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
#List contains the numbers which are accepted from user. 
#Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
#Map function will increase each number by 10.
#Reduce will return product of all that numbers.
#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000
def CheckMaxMin(no):
    if no>=70 and no<=90:
        return True
    else:
        return False

def Filter(arr):
    brr = []
    for i in range(len(arr)):
        if CheckMaxMin(arr[i])==True:
            brr.append(arr[i])
    return brr

def Map(arr):
    for  i in range(len(arr)):
        arr[i]=arr[i] + 10
    return arr

def Reduce(arr):
    sum = 1
    for i in range(len(arr)):
        sum = sum * arr[i]
    return sum

def main():
    arr=[]
    print("Enter the size of list")
    size=int(input())
    for i in range(size):
        print("Elements are :",i+1)
        no=int(input())
        i = i + 1
        arr.append(no)
    print("Display the elements are :",arr)
    ret = Filter(arr)
    print("After filter that list is:",ret)

    ret1 =Map(ret)
    print("After map list is",ret1)
    
    output=Reduce(ret1)
    print("After reduce list is:",output)


if __name__=="__main__":
    main()