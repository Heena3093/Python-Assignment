#10. Write a program which accept name from user and display length of its name.
#Input : Marvellous Output : 10

def findLen(str): 
    counter = 0
    while str[counter:]: 
        counter += 1
    return counter 

def main():
    print("Enter the name")
    name=input()

    ret = findLen(name)
    print("Length of name is :",ret)

if __name__=="__main__":
    main()