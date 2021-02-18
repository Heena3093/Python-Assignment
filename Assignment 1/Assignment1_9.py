#9. Write a program which display first 10 even numbers on screen.
#Output : 2 4 6 8 10 12 14 16 18 20

def DisplayW():
    print("Display First 10 even number")
    i=0 
    while(i<20):      
        i=i+2
        print(i)

def main():
    DisplayW()
   

if __name__=="__main__":
    main()