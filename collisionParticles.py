import pygame # type: ignore
import sys
import random
from parts.particles import Particle
from parts.functions import detectResolve_collsion_PRb, particle_collison

def create_random_particle(count1, count2):
     speed_constant = 1
     particle = Particle(
          radius=10,
          mass= 10,
          displacementX=60*count1,
          displacementY=60*count2,
          velocityX = random.random()*speed_constant if count1 > 0 else random.random()*-speed_constant,
          velocityY = random.random()*speed_constant if count2 > 0 else random.random()*-speed_constant,
          accelerationY=-0.00001
     )
     return particle


def convert_coordinates(x,y,width,height):
     '''
     In the y direction
     one of the '-' performs the coordinate inversion
     the other '-' accounts for the correct shift
     '''
     return (x + width//2), -(y-height//2) 

def get_adjacentCell_particles(x,y,grid):
     adjacent_partilces = []
     height = len(grid)
     width = len(grid[0])

     for dy in [-1,0,1]:
          ny = y + dy
          if ny < 0 or ny >= height:
               continue

          for dx in [-1,0,1]:
               nx = x + dx
               if nx < 0 or nx >= width:
                    continue

               if dx == dy == 0:
                    continue

               adjacent_partilces.extend(grid[ny][nx])
     
     return adjacent_partilces

def check_collisions(list1, list2, checkedSet, restitution):
     for p1 in list1:
          for p2 in list2:
               if p1 is p2:
                    continue

               pair = tuple(sorted((id(p1),id(p2))))
               if pair in checkedSet:
                    continue
               checkedSet.add(pair)

               particle_collison(p1, p2, restitution)

def draw_particle(particle, screen, width, height):
     x, y = convert_coordinates(particle.get_displacementX(), particle.get_displacementY(),width,height)
     pygame.draw.circle(screen, particle.get_colour(), (int(x), int(y)), particle.get_radius())


def main1():
     # Init Pygame
     pygame.init()

     #Screen setup
     WIDTH, HEIGHT = 400, 300
     screen = pygame.display.set_mode((WIDTH, HEIGHT))
     pygame.display.set_caption("Particle Motion Simulation")

     #FPS
     clock = pygame.time.Clock()
     FPS = 100

     #Particles setup
     particles = []
     count1 = -2
     count2 = -2

     for i in range(5):
          count1 = -5
          count2 += 1
          for j in range(5):
               count1 +=1
               particles.append(create_random_particle(count1, count2))

     restitution = 1

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
               detectResolve_collsion_PRb(p,WIDTH,HEIGHT,restitution)
          
          #defernitely works, all collisions accounted for
          for p1 in particles:
               for p2 in particles:
                    if id(p1) <= id(p2):
                         continue
                    particle_collison(p1, p2, restitution)

          '''
          #seperate screen into grid
          cell_size = 50
          grid = [[[]for i in range(WIDTH//cell_size)]for i in range(HEIGHT//cell_size)]
          for p in particles:
               x, y = convert_coordinates(p.get_displacementX(), p.get_displacementY(),WIDTH, HEIGHT)
               grid[int(y//cell_size)][int(x//cell_size)].append(p)
          
          #check collisions
          checked = set()
          for col in range(len(grid)):
               for row in range(len(grid[0])):
                    cell_particles = grid[col][row]
                    neighbour_particles = get_adjacentCell_particles(col,row,grid)

                    #same cell collisions
                    check_collisions(cell_particles, cell_particles, checked, restitution)
                    
                    #neighbouring cell collisions
                    check_collisions(cell_particles, neighbour_particles, checked, restitution)       

          '''
          #draw particles
          for p in particles:
               draw_particle(p,screen,WIDTH, HEIGHT)

          pygame.display.flip()
          clock.tick(FPS)

     pygame.quit()
     sys.exit()

main1()