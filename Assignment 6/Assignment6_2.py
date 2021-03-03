#2. Write a program which contains one class named as Circle.Circle class contains three instance variables as Radius ,Area, Circumference.
#That class contains one class variable as PI which is initialise to 3.14. Inside init method initialise all instance variables to 0.0.
#There are three instance methods inside class as Accept(), CalculateArea(),CalculateCircumference(), Display().Accept method will accept value of Radius from user.
#CalculateArea() method will calculate area of circle and store it into instance variable Area.CalculateCircumference() method will calculate circumference of circle and store it into instance
#variable Circumference.And Display() method will display value of all the instance variables as Radius , Area,Circumference.
#After designing the above class call all instance methods by creating multiple objects.

class Circle:
    PI=3.14
    def __init__(self,radius=0,area=0,circumference=0):
        self.Radius=radius
        self.Area=area
        self.Circumference=circumference

    def CalculateArea(self):
        self.Area= Circle.PI * self.Radius * self.Radius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference= 2 * Circle.PI * self.Radius
        return self.Circumference
    
    def Display(self):
        print("Radius of Circle is :",self.Radius)
        print("Area of Circle is :",self.Area)
        print("Circumference of Circle is :",self.Circumference)
    
    

def main():
    print("Enter the radius : ")
    radius=int(input())

    obj1=Circle(radius)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()
    
if __name__=="__main__":
    main()
