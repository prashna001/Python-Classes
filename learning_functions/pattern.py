#SQUARE
def pattern_square(size=10):
    for i in range(size):
        row ='O'* size
        print(row)
pattern_square(10)




#HOLLOW SQUARE
def pattern_hollow_square(size=10):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1 or j == 0 or j == size-1:
                print('*', end='')
            else:
                print('', end='')
                print(5)






#Rectangle
def pattern_rectangle(rows=5, colum=9):
    for i in range(rows):
       print('#' * colum)
pattern_rectangle(5,9)



#Pyramid
def pattern_pyramid(rows=25):
    for i in range (1, rows+1):
        spaces = ' ' * (rows-i)
        shapes = '$' * (2 * i-1)
        print(spaces + shapes)
pattern_pyramid(25)

#Hollow Pyramid
