a = input("Enter a string: ")

if len(a) >= 3:
    if a.endswith("ing"):
        a = a + "ly"
    else:
        a = a + "ing"

print(a)
