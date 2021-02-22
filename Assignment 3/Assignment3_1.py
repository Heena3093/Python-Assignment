#1.Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130

def Addition(List):
    sum = 0
    for i in range(len(List)):
        sum = sum + List[i]
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
    ret=Addition(arr)
    print("Additon of element is :",ret)

if __name__=="__main__":
    main()