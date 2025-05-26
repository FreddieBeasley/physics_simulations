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
     
     def get_magnitude(self):
          xSquared = (self.getX())**2
          ySquared = (self.getY())**2
          return (xSquared + ySquared)**(1/2)
     
     def get_theta(self):
          return math.atan2(self.getY(), self.getX())
     
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

     #getter - inherits getX and getY and get_theta

     def getZ(self):
          return self.__Zcomponent
     
     def get_magnitude(self):
          xSquared = (self.getX())**2
          ySquared = (self.getY())**2
          zSquared = (self.getZ())**2
          return (xSquared + ySquared + zSquared)**(1/2)

     def get_phi(self):
          phi = math.acos(self.getZ(), self.get_magnitude())
     
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
     
class particle:
     def __init__(self):
          self.__displacement = Vector2(0,0)
          self.__velocity = Vector2(0,0)
          self.__acceleration = Vector2(0, -9.8)

     #getter
     def get_displacementX(self):
          return self.__displacement.getX()

     def get_displacementY(self):
          return self.__displacement.getY()
     
     def get_displacement(self):
          return self.get_displacementX(), self.get_displacementY()
     
     def get_velocityX(self):
          return self.__velocity.getX()
     
     def get_velocityY(self):
          return self.__velocity.getY()
     
     def get_velocity(self):
          return self.get_velocityX(), self.get_velocityY
     
     def get_accelerationX(self):
          return self.__acceleration.getX()
     
     def get_accelerationY(self):
          return self.__acceleration.getY()
     
     def get_acceleration(self):
            return self.get_accelerationX(), self.get_accelerationY
     
     #setters
     def __set_displacementX(self, value):
          self.__displacement.setX(value)
     
     def __set_displacementY(self, value):
          self.__displacement.setY(value)

     def set_displacement(self, Xvalue=None, Yvalue=None):
          if Xvalue is not None:
               self.set_displacementX(Xvalue)

          if Yvalue is not None:
               self.set_displacementY(Yvalue)
     
     def __set_velocityX(self, value):
          self.__velocity.setX(value)
     
     def __set_velocityY(self, value):
          self.__velocity.setY(value)
     
     def set_velocity(self, Xvalue=None, Yvalue=None):
          if Xvalue is not None:
               self.set_velocityX(Xvalue)

          if Yvalue is not None:
               self.set_velocityY(Yvalue)
          
     def __set_accelerationX(self, Xvalue):
          self.__acceleration.setX(Xvalue)
     
     def __set_accelerationY(self, Yvalue):
          self.__acceleration.setY(Yvalue)
     
     def set_acceleration(self, Xvalue, Yvalue):
          if Xvalue is not None:
               self.set_accelerationX(Xvalue)
          
          if Yvalue is not None:
               self.set_accelerationY(Yvalue)
          

     #updater
     def update_displacement(self):
          new_displacementX = self.get_displacementX() + self.get_velocityX()
          new_displacementY = self.get_displacementY() + self.get_velocityY()
     
     def update_velocity(self):
          new_velocityX = self.get_velocityX() + self.get_accelerationX()
          new_velocityY = self.get_velocityY() + self.get_accelerationY()
     
     
     