num = int(input("Enter a number: "))
s = 0  

while num > 0:
    digit = num % 10   
    s += digit          
    num //= 10         

print("The sum of the digits is:", s)
