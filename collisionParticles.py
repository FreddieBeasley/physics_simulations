import pygame
import sys
import random
from parts.particles import Particle
from parts.functions import detectResolve_collsion_PRb, particle_collison

def create_random_particle(count1, count2):
     particle = Particle(
          radius=10,
          mass= 10*random.random(),
          displacementX=60*count1,
          displacementY=60*count2,
          velocityX = random.random() if count1 > 0 else random.random()*-1,
          velocityY = random.random() if count2 > 0 else random.random()*-1,
     )
     return particle


def convert_coordinates(x,y,width,height):
     '''
     In the y direction
     one of the '-' performs the coordinate inversion
     the other '-' accounts for the correct shift
     '''
     return (x + width//2), -(y-height//2) 

def main1():
     # Init Pygame
     pygame.init()

     #Screen setup
     WIDTH, HEIGHT = 800, 600
     screen = pygame.display.set_mode((WIDTH, HEIGHT))
     pygame.display.set_caption("Particle Motion Simulation")

     #FPS
     clock = pygame.time.Clock()
     FPS = 500

     #Particles setup
     particles = []
     count1 = -5
     count2 = -5

     for i in range(10):
          count1 = -5
          count2 += 1
          for j in range(10):
               count1 +=1
               particles.append(create_random_particle(count1, count2))

     restitution = 0.9

     running = True
     while running:
          screen.fill((0, 0, 0))
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running = False

          # Update motion
          for p in particles:
               p.update_velocity()
               p.update_displacement()
               

          for pA in particles:
               for pB in particles:
                    if pA == pB:
                         continue
                    particle_collison(pA, pB, restitution)

          for p in particles:
               detectResolve_collsion_PRb(p,WIDTH,HEIGHT,restitution)

               x, y = convert_coordinates(p.get_displacementX(), p.get_displacementY(),WIDTH,HEIGHT)
               pygame.draw.circle(screen, p.get_colour(), (int(x), int(y)), p.get_radius())






          pygame.display.flip()
          clock.tick(FPS)

     pygame.quit()
     sys.exit()

main1()