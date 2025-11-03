import math

print("Four-digit numbers with all even digits that are perfect squares:")
for number in range(1000,9999):
    digits = str(number)
    if all(int(d) % 2 == 0 for d in digits):
        if int(math.sqrt(number))**2 == number:
            print(number)
