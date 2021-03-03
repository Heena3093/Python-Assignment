#3.Write a recursive program which display below pattern.
#Input : 5
#Output : 5 4 3 2 1

def DisplayP(no):
    i=1
    while no>=i:        
        print(no)
        no=no-1
i=1
def DisplayRec(no):
    global i
    if no>i:                 
        no = no - 1
        print(no)     
        DisplayRec(no)




def main():
    value=5
    DisplayRec(value)

if __name__=="__main__":
    main()