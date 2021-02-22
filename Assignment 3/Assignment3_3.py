#3.Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#Output : 5

def Minimum(list):
    min = list[0]      
    for a in range(len(list)):
        if list[a] < min:
            min = list[a]
    return min

def main():
    arr=[]
    print("Enter the number of elements:")
    size=int(input())
    for i in range(size):
        print("The elemnts are :",i+1)
        no=int(input())
        arr.append(no)
    print("Display the Elements are:",arr)
    ret=Minimum(arr)
    print("Minimum Number is :",ret)

if __name__=="__main__":
    main()