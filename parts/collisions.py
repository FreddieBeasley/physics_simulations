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

def get_centre_distance(particle1, particle2) -> float:
     if not isinstance(particle1, Particle) or not isinstance(particle2, Particle):
          raise TypeError("parametres must a Particle objects")
     
     s1_x, s1_y = particle1.get_displacement()
     s2_x, s2_y = particle2.get_displacement()

     deltaX_squared = (s1_x - s2_x)**2
     deltaY_squared = (s1_y - s2_y)**2

     distance = (deltaX_squared + deltaY_squared)**(1/2)

     return distance