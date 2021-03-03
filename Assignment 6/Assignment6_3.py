#3. Write a program which contains one class named as Arithmetic. Arithmetic class contains three instance variables as Value1 ,Value2.
#Inside init method initialise all instance variables to 0.There are three instance methods inside class as Accept(), Addition(), Subtraction(),
#Multiplication(), Division().Accept method will accept value of Value1 and Value2 from user.Addition() method will perform addition of Value1 ,Value2 and return result.
#Subtraction() method will perform subtraction of Value1 ,Value2 and return result.Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
#Division() method will perform division of Value1 ,Value2 and return result.After designing the above class call all instance methods by creating multiple objects.



class Arithmetic:
    def __init__(self,i=0,j=0):
        self.value1=i
        self.value2=j
    
    def Addition(self):
        return self.value1 +self.value2
    
    def Substraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        return self.value1/self.value2

def main():
    value1=int(input("Enter First number : "))
    value2=int(input("Enter Second number : "))
    
    obj1=Arithmetic(value1,value2)
    obj2=Arithmetic(value1,value2)

    Ret = obj1.Addition()
    print("Addition is :",Ret)

    Ret=obj1.Substraction()
    print("Substraction is :",Ret)

    Ret=obj1.Multiplication()
    print("Multiplication is :",Ret)

    Ret=obj1.Division()
    print("Division is :",Ret)

if __name__=="__main__":
    main()
    