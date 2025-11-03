num = int(input("Enter a number: "))

def sum_of_digits(n):
    s = 0
    while n > 0:
        digit = n % 10
        s = s + digit
        n = n // 10
    print("Sum of digits of the number:", s)

sum_of_digits(num)
