import math
class Vector2:
     #initialise
     def __init__(self, Xcomponent, Ycomponent):
          self.__Xcomponent = Xcomponent
          self.__Ycomponent = Ycomponent
     
     #getter
     def getX(self):
          return self.__Xcomponent
     
     def getY(self):
          return self.__Ycomponent
     
     def get_cartesian(self):
          return [self.getX(), self.getY()]
     
     def get_magnitude(self):
          xSquared = (self.getX())**2
          ySquared = (self.getY())**2
          return (xSquared + ySquared)**(1/2)
     
     def get_direction(self):
          return math.atan2(self.getY(), self.getX())
     
     def get_polar(self):
          return (self.get_magnitude(), self.get_direction())

     
     #setter
     def setX(self, value):
          self.__Xcomponent = value
     
     def setY(self, value):
          self.__Ycomponent = value
     
     def set(self, Xvalue, Yvalue):
          self.setX(Xvalue)
          self.setY(Yvalue)
     
     #updater
     def updateX(self, dValue):
          self.__Xcomponent += dValue
     
     def updateY(self, dValue):
          self.__Ycomponent += dValue
     
     def update(self, dXvalue, dYvalue):
          self.updateX(dXvalue)
          self.updateY(dYvalue)

