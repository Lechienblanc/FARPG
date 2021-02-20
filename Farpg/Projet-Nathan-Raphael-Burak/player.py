import pygame
pygame.init()


#### j'ai essayé pygame sans réussite #### Raphael
class Player (pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 1000
        self.max_health = 10000
        self.attack = 10 
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300



pygame.display.set_caption("Project RPG")
screen = pygame.display.set_mode((1080, 720))

player = Player()

running=True

while running:

    screen.blit(player.image, player.rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False  
            pygame.quit()
            print("fermeture du jeu")
