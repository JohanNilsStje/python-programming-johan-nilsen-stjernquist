class Geometry_common:
  def __init__(self,x,y):
    #Positioner i Koordinatsystem
    self._x = int(x)
    self._y = int(y)

  def get_x(self):
    return self._x
  def get_y(self):
    return self._y
  def set_x(self, value):
    self._x = value
  def set_y(self, value):
    self._y = value
  def translate(self,x,y):
    try:
      self._x = int(x)
      self._y = int(y)
    except Exception:
      print("You need to enter int or float. Example translate(int,int), translate(float,float) if you do translate(str, str) this message will apear!")
    pass

##################
class Circle(Geometry_common):
  def __init__(self, x, y, radius):
    super().__init__(x,y)
    self.radius = radius
  

  #Area / Circumfrance for Circle
  def set_radius(self, value):
    self.radius = value

  def get_area(self):
    area = 3.1415 * (self.radius*self.radius)
    print(f"Area = {area}")
    return area
  
  def get_circumfrence(self):
    # C = 2πr
    circumfrance = 3.14 * 2 * self.radius
    print(f"Circumfrance = {circumfrance}")
    return circumfrance
  def is_unit_circle(self):
    return self.radius == 1
  
##################
class Rectangle(Geometry_common):
  def __init__(self, x, y, side1, side2):
    super().__init__(x,y)
    self.side1 = side1
    self.side2 = side2

  def set_sides(self,side1,side2):
    self.side1 = side1
    self.side2 = side2
    
  #Area / Circumfrance for Rectangle
  def get_area(self):
    area = self.side1 * self.side2
    print(f"Area = {area}")
    return area
  def get_circumfrence(self):
    circumfrance = self.side1*2 + self.side2*2
    print(f"Circumfrance = {circumfrance}")
    return circumfrance
  
  def is_square(self):
    return self.side1 == self.side2
    
  def __str__(self) -> str:
    
    pass
  def __repr__(self) -> str:
    
    pass