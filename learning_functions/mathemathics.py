# Adding two numbers
def add_two_num(n1, n2):
    """
    This function will be used to add odd and even numbers.
    :param n1: This is the odd number.
    :param n2: This is the even number.
    :return: Returns the sum of n1 and n2 as Float/Int.
    """
    total = n1 + n2
    return total

# Odd or Even Numbers
def odd_even(number):
    """
    Determines if a number is odd or even.
    :param number: The number to classify.
    :return: A string indicating if the number is odd or even.
    """
    if number == 0:
        return "0 cannot be classified"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Odd or Even for a List of Numbers
def odd_even_list(numbers):
    """
    Classifies a list of numbers as odd or even.
    :param numbers: A list of integers.
    :return: A list of tuples with the number and its classification.
    """
    result = []
    for number in numbers:
        value = odd_even(number)
        result.append((number, value))
    return result


# Combining 1 & 2
def odd_even_final(num, multiple):
    """
    A placeholder function to demonstrate combining operations.
    :param num: A number or list of numbers to process.
    :param multiple: A flag indicating if multiple numbers are processed.
    :return: Placeholder return for demonstration.
    """
    if multiple:
        return odd_even_list([1, 3, 5, 4])
    else:
        return odd_even(num)
print(odd_even_final([1,3,5,4,], True))



#Palindrome
def is_palindrome(num):
    num_str = str(num)
    length = len(num_str)
    for i in range(length // 2):
        if num_str[i] != num_str[length - 1 - i]:
            return False
    return True
number = 123
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


def is_palindrome(num):
        num_str = str(num)
        reversed_num_str = ""
        for char in num_str:
            reversed_num_str = char + reversed_num_str
        if num_str == reversed_num_str:
            return True
        else:
            return False

num = 124
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")


