#Write a program which display 5 times Marvellous on screen.
#Output : Marvellous
#Marvellous
#Marvellous
#Marvellous
#Marvellous

def Display(no):
    for i in range(no):
        print("Marvellous")

def main():

    print("Enter number to print msg")
    value=int(input())

    Display(value)


if __name__=="__main__":
    main()