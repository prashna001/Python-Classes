def two_numbers(a,b):
    def add():
        return a+b
    def subtract ():
        return a-b
    def multiple ():
        return a*b
    def divide():
        return a/b
    return {'add': add(), 'subtract':subtract(),'multiple': multiple(), 'divide': divide()}

func = two_numbers(1,2)
print(func)


