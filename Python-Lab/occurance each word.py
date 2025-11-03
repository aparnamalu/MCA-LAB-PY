string=input("enter the line of text:")
word=input("enter the word:")
a=[]
a=string.split(" ")
count=0
for i in range(0,len(a)):
    if(word==a[i]):
         count=count+1
print("count of the word is:")
print(count)
