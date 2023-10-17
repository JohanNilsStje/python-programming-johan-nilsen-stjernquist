from geometry_shapes import *


undefined_shape = Geometry_common(x=0,y=0)

cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
cirkel2 = Circle(x=0,y=0, radius=1)
rektangel = Rectangle(x=0,y=0,side1=1, side2=1)



print(f"{cirkel1.radius == cirkel2.radius} cirkel1.radius == cirkel2.radius")
print(f"{cirkel2==rektangel} cirkel2 == rektangel") # False
print(f"{cirkel1.is_inside(0.5, 0.5)} is_inside(0.5,0.5)") # True 
cirkel1.translate(5,5)
print(f"{cirkel1.is_inside(0.5, 0.5)} is_inside(0.5,0.5)") # False
cirkel1.translate(1.5,5) # ge ValueError med lämplig kommentar

repr(rektangel)
print(rektangel)
repr(cirkel1)
print(cirkel1)
repr(undefined_shape)
print(undefined_shape)

print(Geometry_common.__doc__)


print(rektangel.is_inside(0.5,0.5))
rektangel.translate(3,3)
print(rektangel.is_inside(0.5,0.5))

print(cirkel1.area)
print(cirkel1.circumfrance)

print(repr(cirkel1))
print(cirkel1)

print(cirkel1 > cirkel2)

#Chat GPT wrote this testcode:
circle = Circle(x=0, y=0, radius=3)
# Test methods and properties for the Circle object
print("Circle Properties:")
print("Radius:", circle.radius)
print("Area:", circle.area)
print("Circumference:", circle.circumfrance)
print("Is a unit circle:", circle.is_unit_circle())
print("Is (2, 2) inside the circle:", circle.is_inside(2, 2))

# Create a Rectangle object
rectangle = Rectangle(x=0, y=0, side1=4, side2=5)

# Test methods and properties for the Rectangle object
print("\nRectangle Properties:")
print("Side 1:", rectangle.side1)
print("Side 2:", rectangle.side2)
print("Area:", rectangle.area)
print("Circumference:", rectangle.circumfrance)
print("Is a square:", rectangle.is_square())
print("Is (2, 2) inside the rectangle:", rectangle.is_inside(2, 2))