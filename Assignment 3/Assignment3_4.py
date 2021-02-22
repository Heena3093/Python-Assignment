#4.Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3
def DisplayCount(LIST,x):
    cnt = 0
    for i in range(len(LIST)):       
        if LIST[i]==x:
            cnt=cnt+1
    return cnt

def main():
    arr=[]
    print("Enter the number of elements:")
    size=int(input())
    for i in range(size):
        print("The elemnts are :",i+1)
        no=int(input())
        arr.append(no)
    print("Display the Elements are:",arr)
    print("Elemnt to the search")
    no=int(input())
    ret=DisplayCount(arr,no)
    print("Number of count is :",ret)

if __name__=="__main__":
    main()