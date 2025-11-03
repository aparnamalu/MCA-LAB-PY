s = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_list = []

for char in s:
    if char in vowels:
        vowel_list.append(char)

print("List of vowels:", vowel_list)
