class Calculator:
    def __init__(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        return float(self.first+self.second)
    
    def sub(self):
        return float(self.first-self.second)
    
    def multiply(self):
        return float(self.first*self.second)
    
    def divide(self):
        return float(self.first/self.second)


first=float(input("Please enter first value: "))
second=float(input("Please enter second value: "))
calculator=Calculator(first,second)

print(calculator.add())
print(calculator.sub())
print(calculator.multiply())
print(calculator.divide())