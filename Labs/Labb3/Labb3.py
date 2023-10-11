from geometry_shapes import *

cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
cirkel2 = Circle(x=1,y=1, radius=1)
rektangel = Rectangle(x=0,y=0,side1=1, side2=1)

print(f"{cirkel1.radius == cirkel2.radius} cirkel1.radius == cirkel2.radius") # Not sure how I sohuld make cirkel1 and cirkel2 return the radius when the object is called
print(f"{cirkel2==rektangel} cirkel2 == rektangel") # False (works somehow?)
print(f"{cirkel1.is_inside(0.5, 0.5)} is_inside(0.5,0.5)") # True 
cirkel1.translate(5,5)
print(f"{cirkel1.is_inside(0.5, 0.5)} is_inside(0.5,0.5)") # False
cirkel1.translate(1.5,5) # ge ValueError med lämplig kommentar

print(rektangel)