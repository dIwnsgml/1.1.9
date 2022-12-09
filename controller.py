import pygame
pygame.init()
def controller():
  while True:
    key_input = pygame.key.get_pressed()
    if(key_input[pygame.K_LEFT]):
      print("a")

controller()