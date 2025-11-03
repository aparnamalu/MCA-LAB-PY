n = int(input("Enter the number of n terms: "))

f1 = 0
f2 = 1
count = 1

print("Fibonacci series of", n, "terms:", end=" ")

while count <= n:
    print(f1, end=" ")
    next_term = f1 + f2
    f1 = f2
    f2 = next_term
    count += 1
