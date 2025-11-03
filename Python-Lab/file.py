filename=input("enter the filename:")
if '.'in filename:
    extension=filename.split('.')[-1]
    print(f"The extension of the file is:{extension}")
else:
     print("The file has no extension.")
