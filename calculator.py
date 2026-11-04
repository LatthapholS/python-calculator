class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b != abs(b):
            b =  abs(b)
            for i in range(b):
                        result = self.add(result, -a)
        else:
            for i in range(b):
                result = self.add(result, a)
        return result


    def divide(self, a, b):
        result = 0
        if b == 0:
             raise ZeroDivisionError(" division by zero")
        if b == abs(b):
            while a >= b:
                a = self.subtract(a, b)
                result += 1
        elif b != abs(b):
            b = abs(b)

            while a >= b:
                a = self.subtract(a, b)
                result -= 1
                    
        return result



    


    def modulo(self, a, b):
        calc = Calculator()
        if a == abs(a) and b == abs(b): 
            while b <= a:
                a = a-b
            return a
        elif (a != abs(a) and b == abs(b) )or (a == abs(a) and b != abs(b)):
             return a - (calc.multiply(calc.divide(a, b) -1, b) )
        else:
             return a - (calc.multiply(calc.divide(abs(a), abs(b)) , b) )

             

    

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
