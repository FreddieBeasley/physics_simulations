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

class Vector3(Vector2):
     def __init__(self, Xcomponent, Ycomponent, Zcomponent):
          super().__init__(Xcomponent, Ycomponent)

          self.__Zcomponent = Zcomponent

     #getter - inherits getX and getY

     def getZ(self):
          return self.__Zcomponent
     
     def get_cartesian(self):
          return [self.getX(), self.getY(), self.getZ()]
     
     def get_magnitude(self):
          xSquared = (self.getX())**2
          ySquared = (self.getY())**2
          zSquared = (self.getZ())**2
          return (xSquared + ySquared + zSquared)**(1/2)
     
     def get_theta(self):
          theta = math.atan2(self.getY(), self.get_X())

     def get_phi(self):
          phi = math.acos(self.getZ(), self.get_magnitude())
     
     def get_direction(self):
          return [self.get_theta(), self.get_phi()]
     
     def get_polar(self):
          return [self.get_magnitude(), self.get_theta(), self.get_phi()]
     
     #setter - inherits setX and setY
     def setZ(self, value):
          self.__Zcomponent = value
     
     def set(self, Xvalue, Yvalue, Zvalue):
          self.setX(Xvalue)
          self.setY(Yvalue)
          self.getZ(Zvalue)
     
     #updater - inherits updateX and updateY
     def updateZ(self, dZvalue):
          self.__Zcomponent += dZvalue
     
     def update(self, dXvalue, dYvalue, dZvalue):
          self.updateX(dXvalue)
          self.updateY(dYvalue)
          self.updateZ(dZvalue)
     
