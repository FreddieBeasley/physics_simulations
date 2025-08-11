from parts.simEquations import solve_simultaneos_equation
from parts.particles import Particle

def resolve_collision_1d(m1, m2, u1, u2, restitution) -> float:
     
     """
     CONSERVATION OF MOMENTUM
     (m1*u1) + (m2*u2) = (m1*v1 + m2*v2)

     Av1 + Bv2 = C
     [m1, m2, m1*u1 + m2*u2]
     """
     
     equationA = [m1, m2, m1*u1 + m2*u2]

     """
     CONSERVATION OF KENETIC ENERGY WITH RESPECT TO RESTITUTION

     -e = (v1 - v2) / (u1 - u2)
     -e*u1 +e*u2 = v1 - v2
     -v1 + v2 = e*u1 - e*u2

     Av1 + Bv2 = C
     [-1, 1, e*u1 - e*u2]

     """

     equationB = [-1, 1, restitution*u1 - restitution*u2]


     #Solving equations
     v1, v2 = solve_simultaneos_equation(equationA, equationB)

     return v1, v2

def get_deltaX_distance(particle1, particle2) -> float:
     if not isinstance(particle1, Particle) or not isinstance(particle2, Particle):
          raise TypeError("parameters must be particle objects")
     
     return abs(particle1.get_displacementX() - particle2.get_displacementX())

def get_deltaY_distance(particle1, particle2) -> float:
     if not isinstance(particle1, Particle) or not isinstance(particle2, Particle):
          raise TypeError("parameters must be particle objects")
     
     return abs(particle1.get_displacementY() - particle2.get_displacementY())

def magnitude_2d(value1:float, value2:float) -> float:
     return ((value1**2) + (value2**2))**(1/2)

def get_centre_distance(particle1, particle2) -> float:
     return magnitude_2d(get_deltaX_distance(particle1, particle2),get_deltaY_distance(particle1, particle2))
