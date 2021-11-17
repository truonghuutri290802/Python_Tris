import pygame 

pygame.init()

screen = pygame.display.set_mode((500,600))

grey = (120,120,120)
white = (255,255,255)
running = True
 
while running:
    screen.fill(grey)
    pygame.draw.rect(screen,white,(100,50,50,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                print("XXX")
    pygame.display.flip()
pygame.quit()