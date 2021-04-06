import pygame
import random

# pygame 초기화
pygame.init()

# 게임 화면 구현 (노트북 화면과 호환되도록 하였음..)
screen = pygame.display.set_mode((900, 650))

# Background
background = pygame.image.load('background.jpg')

# Title and Icon
pygame.display.set_caption("Kiki's Delivery Service")
icon = pygame.image.load('witch.png')
pygame.display.set_icon(icon)

# Player 구현
playerImg = pygame.image.load('kiki.png')
playerX = 0
playerY = 200

playerX_change = 0
playerY_change = 0

# Enemy 구현(까마귀)
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('raven.png'))
    enemyX.append(random.randint(200, 900))
    enemyY.append(random.randint(0, 650))
    enemyX_change.append(-1)
    enemyY_change.append(-1)

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

# 게임 루프
running = True
while running:
    # screen.fill((0,51,255))

    # Background Image
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키를 눌렀을 때 움직이는 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # player가 화면 밖으로 나갈 경우
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0

    elif playerX >= 850:
        playerX = 850

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0

    elif playerY >= 550:
        playerY = 550

        
    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
            

        elif enemyX[i] >= 850:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]   

        enemy(enemyX[i], enemyY[i], i)

    #enemyY += enemyY_change
    #if enemyY <= 0:
        #enemyY_change = 0.4

    #elif enemyY >= 550:
        #enemyY_change = -0.4
    
    player(playerX, playerY)
    
    pygame.display.update()

