import pygame

# pygame 초기화
pygame.init()

# 게임 화면 구현
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Kiki's Delivery Service")
icon = pygame.image.load('witch.png')
pygame.display.set_icon(icon)

# Player 구현
playerImg = pygame.image.load('kiki.png')
playerX = 0
playerY = 200


def player(x,y):
    screen.blit(playerImg,(x,y))



# 게임 루프
running = True
while running:
    screen.fill((0,51,255))
    playerX += 0.2
    #print(playerX)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    player(playerX, playerY)
    pygame.display.update()
