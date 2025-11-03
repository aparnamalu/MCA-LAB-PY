square = lambda a: a * a
rectangle = lambda l, b: l * b
triangle = lambda b, h: 0.5 * b * h

a = float(input("Enter side of square: "))
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
base = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))

print("Area of square:", square(a))
print("Area of rectangle:", rectangle(l, b))
print("Area of triangle:", triangle(base, h))
