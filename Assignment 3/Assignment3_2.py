#2.Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56

def Maximum(list):
    max = list[0]      
    for a in range(len(list)):
        if list[a] > max:
            max = list[a]
    return max

def main():
    arr=[]
    print("Enter the number of elements:")
    size=int(input())
    for i in range(size):
        print("The elemnts are :",i+1)
        no=int(input())
        arr.append(no)
    print("Display the Elements are:",arr)
    ret=Maximum(arr)
    print("Maximum Number is :",ret)

if __name__=="__main__":
    main()

