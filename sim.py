import pygame
import sys
from time import sleep
from bouncingParticle import Particle

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
     FPS = 200

     #Particle setup
     p = Particle()

     RADIUS = 40
     COLOR = (255, 0, 0)
     restitution = 0.8

     running = True
     while running:
          screen.fill((255, 255, 255))  # White background

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running = False

          # Update motion
          p.update_velocity()
          p.update_displacement()

          x, y = convert_coordinates(p.get_displacementX(), p.get_displacementY(),WIDTH,HEIGHT)

          # Bounce off the floor
          screen_bottom = -(HEIGHT//2)
          screen_top = (HEIGHT//2)

          if p.get_displacementY() + RADIUS >= screen_top:
               p.set_displacement(Yvalue = screen_top - RADIUS)
               p.set_velocity(Yvalue= -abs(p.get_velocityY()*restitution))

          if p.get_displacementY() - RADIUS <= screen_bottom:
               p.set_displacement(Yvalue = screen_bottom + RADIUS)
               p.set_velocity(Yvalue= abs(p.get_velocityY()*restitution))

          #Bounce off the wall
          screen_left = -(WIDTH//2)
          screen_right = (WIDTH//2)

          if p.get_displacementX() - RADIUS <= screen_left:
               p.set_displacement(Xvalue = screen_left + RADIUS)
               p.set_velocity(Xvalue= abs(p.get_velocityX()*restitution))

          if p.get_displacementX() + RADIUS >= screen_right:
               p.set_displacement(Xvalue = screen_right - RADIUS)
               p.set_velocity(Xvalue= -abs(p.get_velocityX()*restitution))
               
          # Draw particle
          pygame.draw.circle(screen, COLOR, (int(x), int(y)), RADIUS)

          pygame.display.flip()
          clock.tick(FPS)

     pygame.quit()
     sys.exit()

main1()