#2. Write a recursive program which display below pattern.
#Input : 5
#Output : 1 2 3 4 5
def Display(no):
    i=1
    while no>=i:        
        print(i)
        i=i+1
    
i=0
def DisplayRec(no):
    global i
    if i<no:         
        i = i + 1
        print(i)
        DisplayRec(no)

def main():
    value=5
    DisplayRec(value)

if __name__=="__main__":
    main()
