words = input("Enter words separated by spaces: ").split()
longest = max(len(word) for word in words)
print("Length of the longest word is:", longest)
