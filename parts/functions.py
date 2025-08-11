from parts.collisions import *
from parts.particles import Particle



def detectResolve_collsion_PRb(particle, screen_width, screen_height, restitution):

     # Bounce off the floor
     screen_bottom = -(screen_height//2)
     screen_top = (screen_height//2)

     if particle.get_displacementY() + particle.get_radius() >= screen_top:
          particle.set_displacement(Yvalue = screen_top - particle.get_radius())
          particle.set_velocity(Yvalue= -abs(particle.get_velocityY()*restitution))

     if particle.get_displacementY() - particle.get_radius() <= screen_bottom:
          particle.set_displacement(Yvalue = screen_bottom + particle.get_radius())
          particle.set_velocity(Yvalue= abs(particle.get_velocityY()*restitution))

     #Bounce off the wall
     screen_left = -(screen_width//2)
     screen_right = (screen_width//2)

     if particle.get_displacementX() - particle.get_radius() <= screen_left:
          particle.set_displacement(Xvalue = screen_left + particle.get_radius())
          particle.set_velocity(Xvalue= abs(particle.get_velocityX()*restitution))

     if particle.get_displacementX() + particle.get_radius() >= screen_right:
          particle.set_displacement(Xvalue = screen_right - particle.get_radius())
          particle.set_velocity(Xvalue= -abs(particle.get_velocityX()*restitution))

def resolve_collision_2d(particle1 :Particle, particle2: Particle, restitution):
     #velocity
     u1_x, u1_y = particle1.get_velocity()
     u2_x, u2_y = particle2.get_velocity()

     
     v1_x, v2_x = resolve_collision_1d(particle1.get_mass(), particle2.get_mass(), u1_x, u2_x, restitution) #solve in X direction
     v1_y, v2_y = resolve_collision_1d(particle1.get_mass(), particle2.get_mass(), u1_y, u2_y, restitution) #resolve in Y direction

     #spin
     '''
     tbd
     '''

     #updating objects' attributes
     particle1.set_velocity(v1_x, v1_y)
     particle2.set_velocity(v2_x, v2_y)

def resolve_overlap(particle1:Particle, particle2:Particle):
     deltaX = get_deltaX_distance(particle1, particle2)
     deltaY = get_deltaY_distance(particle1, particle2)
     distance = get_centre_distance(particle1, particle2)
     buffer = particle1.get_radius() + particle2.get_radius()

     if distance == 0:
          distance = 0.001 #prevents devision by 0

     overlap = buffer - distance

     if overlap == 0:
          return
     
     #speeds
     speed1 = magnitude_2d(particle1.get_velocityX(), particle1.get_velocityY())
     speed2 = magnitude_2d(particle2.get_velocityX(), particle2.get_velocityY())
 
     #masses
     mass1 = particle1.get_mass()
     mass2 = particle2.get_mass()

     #inertias
     momentum1 = mass1 * speed1
     momentum2 = mass2 * speed2

     momentum = momentum1 + momentum2

     backtrack_distance1 = (momentum1/momentum) * overlap
     backtrack_distance2 = (momentum2/momentum) * overlap

     kx = deltaX / distance
     ky = deltaY / distance

     #prevent sticking


     particle1.set_displacement(
          Xvalue = particle1.get_displacementX() - (kx*backtrack_distance1),
          Yvalue = particle1.get_displacementY() - (ky*backtrack_distance1)
     )
     particle2.set_displacement(
          Xvalue = particle2.get_displacementX() - (kx*backtrack_distance2),
          Yvalue = particle2.get_displacementY() - (ky*backtrack_distance2)
     )



def particle_collison(particle1:Particle, particle2:Particle, restitution) -> bool:
     distance = get_centre_distance(particle1, particle2)
     buffer = particle1.get_radius() + particle2.get_radius()

     if distance > buffer: #No collision
          return
     
     overlap = buffer - distance
     
     if distance < buffer:
          resolve_overlap(particle1, particle2)
          resolve_collision_2d(particle1, particle2, restitution)

     '''
     count = 0
     fraction = 0.1
     while distance < buffer:

          particle1.backtrack(fraction)
          particle2.backtrack(fraction)

          count += 1
          distance = get_centre_distance(particle1, particle2)
     
     
     resolve_collision_2d(particle1, particle2,restitution=restitution)

     for i in range(count):
          particle1.forwardtrack(fraction)
          particle2.forwardtrack(fraction)
     '''

     #calulate backtracking:


