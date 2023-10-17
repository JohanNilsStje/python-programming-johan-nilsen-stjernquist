import math
class Geometry_common:
  """
  Parent Class.
  This class is used to build simple geometry shapes.
  Contains fuctions and properties such as
  get_x, set_x, get_y, set_y, translate(x,y) 
  comparators for <= < == > >= (Checks if compared object contains atr radius and area)
  It also contains property for area and circumfrance
  """
  def __init__(self,x,y):
    #Positioner i Koordinatsystem
    self._x = int(x)
    self._y = int(y)

  @property
  def area(self):
    return None
  @property
  def circumfrance(self):
    return None

  def get_x(self):
    """Returns the x value of the object"""
    return self._x
  def get_y(self):
    """Returns the y value of the object"""
    return self._y
  def set_x(self, value):
    """Sets the x value of the object"""
    self._x = value
  def set_y(self, value):
    """Sets the y value of the object"""
    self._y = value
  def translate(self,x,y):
    """Sets the x and y value of the object"""
    try:
      self._x = int(x)
      self._y = int(y)
    except Exception:
      print("You need to enter int or float. Example translate(int,int), translate(float,float) if you do translate(str, str) this message will apear!")
    pass

  #Comparators magic methods ### The compare method was  taken from ChatGPT before I had written all the code in blocks but ChatGPT reduced the code
  def _compare_attributes(self, other, comparison_operator):
    if hasattr(other, "radius") and hasattr(self, "radius"):
      return comparison_operator(self.radius, other.radius)
    elif hasattr(other, "area") and hasattr(self, "area"):
      return comparison_operator(self.area, other.area)
    else:
      raise ValueError("Can't compare")

  def __eq__(self, other):
    return self._compare_attributes(other, lambda a, b: a == b)

  def __lt__(self, other):
    return self._compare_attributes(other, lambda a, b: a < b)

  def __gt__(self, other):
    return self._compare_attributes(other, lambda a, b: a > b)

  def __le__(self, other):
    return self._compare_attributes(other, lambda a, b: a <= b)

  def __ge__(self, other):
    return self._compare_attributes(other, lambda a, b: a >= b)
  
  def __str__(self) -> str:
    return f'Super Class that is used to build Circles and Rectangles'
  def __repr__(self):
    return f"When building a geometry shape it is used as: class ShapeName(Geometry_common):"

##################
class Circle(Geometry_common):
  """The Circle class.
  Is used to build a circle object with custom fuctions such as: set_radius(radius), is_unit_circle(), is_inside(input_x,input_y)
  it also contains property for area and circumfrance
  """
  def __init__(self, x, y, radius):
    """Initialize a Circle object with the given coordinates and radius."""
    super().__init__(x,y)
    self.radius = radius
     
  def set_radius(self, value):
    """Set the radius of the circle."""
    self.radius = value
  #Area / Circumfrance for Circle
  @property
  def area(self):
    """Area property for the Circle class"""
    return math.pi * (self.radius*self.radius)
  @property
  def circumfrance(self):
    """Circumfrance property for the Circle class"""
    return math.pi * 2 * self.radius
  
  def is_unit_circle(self):
    """Checks if Circle object is a unit circle. A unit circle is a circle with radius of 1"""
    return self.radius == 1
  
  def is_inside(self,input_x,input_y):
    """Checks if the input coordinates is within the Circles radius"""
    return math.dist([self.get_x(),self.get_y()],[input_x,input_y]) < self.radius
  
  def __str__(self) -> str:
    return f'Circle class that is a child of Geometry_common class'
  def __repr__(self): 
    return f"Circle(x = {self._x}, y = {self._y}, radius = {self.radius})"



##################
class Rectangle(Geometry_common):
  """A class for creating rectangle objects."""
  def __init__(self, x, y, side1, side2):
    """Initialize a Rectangle object with x,y coordinates and side1, side2 of the Rectangle"""
    super().__init__(x,y)
    self.side1 = side1
    self.side2 = side2

  def set_sides(self,side1,side2):
    """Sets the side of the rectangle"""
    self.side1 = side1
    self.side2 = side2
  
  #Area / Circumfrance for Rectangle
  @property
  def area(self):
    """Area property for the Rectangle Class"""
    return self.side1 * self.side2
  @property
  def circumfrance(self):
    """Circumfrance property for the Rectangle Class"""
    return self.side1*2 + self.side2*2
  
  def is_square(self):
    """Checks if the object is a square. Returns True if side1 == side2 otherwise returns False"""
    return self.side1 == self.side2
  
  def is_inside(self, x, y): #Used chatGPT 3 to get this function
    """Check if a point is inside the rectangle.

        Args:
            x (float or int): The x-coordinate of the point.
            y (float or int): The y-coordinate of the point.

        Returns:
            bool: True if the point is inside the rectangle; False otherwise.

        Example:
            rect = Rectangle(x=0, y=0, side1=4, side2=5)
            result = rect.is_inside(2, 2)
            # result should be True
        """
    left_boundary = self._x - self.side1 / 2
    right_boundary = self._x + self.side1 / 2
    top_boundary = self._y + self.side2 / 2
    bottom_boundary = self._y - self.side2 / 2
    return left_boundary <= x <= right_boundary and bottom_boundary <= y <= top_boundary
  
  def __str__(self) -> str:
    return f'Rectangle class that is a child of Geometry_common class'
  def __repr__(self):
    return f"Rectangle(x = {self._x}, y = {self._y}, side1 = {self.side1}, side2 = {self.side2})"