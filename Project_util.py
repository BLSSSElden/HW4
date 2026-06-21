def sum_digits(number):
    total = 0
    for digit_char in str(abs(number)):
        total += int(digit_char)
    return total

def count_digits(number):
    return len(str(abs(number)))

def max_digit(number):
    digits = [int(d) for d in str(abs(number))]
    return max(digits) if digits else None

def min_digit(number):
    digits = [int(d) for d in str(abs(number))]
    return min(digits) if digits else None

def is_even(number):
    return number % 2 == 0

def multiply_digits(number):
    digits = [int(d) for d in str(abs(number))]
    result = 1
    for d in digits:
        result *= d
    return result if digits else 0

def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

def is_palindrome(n):
    s = str(abs(n))
    return s == s[::-1]

def count_even_digits(n):
    return sum(1 for d in str(abs(n)) if int(d) % 2 == 0)

def count_odd_digits(n):
    return sum(1 for d in str(abs(n)) if int(d) % 2 != 0)

def first_digit(number):
    return int(str(abs(number))[0])

def last_digit(number):
    return abs(number) % 10

def sum_even_digits(number):
    total = 0
    for d in str(abs(number)):
        digit = int(d)
        if digit % 2 == 0:
            total += digit
    return total


def sum_odd_digits(number):
    total = 0
    for d in str(abs(number)):
        digit = int(d)
        if digit % 2 == 1:
            total += digit
    return total

def square_number(number):
    return number ** 2

def cube_number(number):
    return number ** 3
def average_digit(number):
    digits = [int(d) for d in str(abs(number))]
    return sum(digits) / len(digits) if digits else 0
def is_positive(number):
    return number > 0
def is_negative(number):
    return number < 0