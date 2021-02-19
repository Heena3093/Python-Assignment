#6. Write a program which accept one number and display below pattern.
#Input : 5    Output : * * * * *
#                      * * * *
#                      * * *
 #                     * *
 #                     *

def DisplayP(value):
         
    for i in range(value + 1, 0, -1):    
        print("\r")
        for j in range(0, i - 1):  
            print("*", end=' ')  
    print(" ")      
            
def main():
    print("Enter number to print pattern")
    no=int(input())
    DisplayP(no)


if __name__=="__main__":
    main()
