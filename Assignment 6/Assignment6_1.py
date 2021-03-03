#1.Write a program which contains one class named as Demo.Demo class contains two instance variables as no1 ,no2.
#That class contains one class variable as Value.There are two instance methods of class as Fun and Gun which displays values of instance variables.
#Initialise instance variable in init method by accepting the values from user.

class Demo:
    Value=10
    def __init__(self,i,j):
        print("Inside constructor")
        self.no1=i
        self.no2=j
    
    def __del__(self):
        print("Inside the destructor")

    def Fun(self):
        print("Inside the fun ")
        print(self.no1,self.no2)

    def Gun(self):
        print("Inside the gun")
        print(self.no1,self.no2)

def main():
  
    no1=int(input("Enter first number :"))
    no2=int(input("Enter second number :"))

    Obj1 = Demo(no1,no2)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

    del Obj1
    del Obj2

if __name__=="__main__":
    main()

