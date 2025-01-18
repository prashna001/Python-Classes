
def function(a, b, *args):
    print(a)
    print(b)
    print(args)


function(1, 2, 3, 4, 5, 6)


def function(a, b, *numbers, **kwargs):
    print(a)
    print(b)
    print(numbers, type(numbers))
    print(kwargs, type(kwargs))

function(1, 2, 3, 4, 5, 6, name ='Sahil')


print(type(function))


'''
Scope of variable in python
usage of variable - Y/N

'''



def incrementor(increment):
    def inner(x):
        return x + increment
        return
increment_by_2 = incrementor(2)

'''
this is a generator function
'''

C:\Users\user\PycharmProjects\PythonProject1


