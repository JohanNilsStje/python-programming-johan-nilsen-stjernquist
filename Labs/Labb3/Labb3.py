from geometry_shapes import *

cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
cirkel2 = Circle(x=1,y=1, radius=1)
rektangel = Rectangle(x=0,y=0,side1=1, side2=1)

print(cirkel1.is_unit_circle() == cirkel2.is_unit_circle()) # Funkar ifall jag använder is_unit_circle och jämför
print(cirkel2==rektangel) # False (works somehow?)
# print(cirkel1.is_inside(0.5, 0.5)) # True
cirkel1.translate(5,5)
# print(cirkel1.is_inside(0.5, 0.5)) # False
cirkel1.translate(1.5,5) # ge ValueError med lämplig kommentar
