name = input("Enter a string: ")
s = name[0]
name = s + name[1:].replace(s, '&')
print(name)
