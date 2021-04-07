import pygame
import random

# pygame 초기화
pygame.init()

# 게임 화면 구현
# 15인치 화면에 호환되도록 하였기 때문에
# 다른 desktop에서 보면 작게 보일 수 있습니다...)
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
    enemyX_change.append(-2)
    enemyY_change.append(-2)

# Score
score_value = 0
font = pygame.font.Font('Goyang.ttf',40)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score:" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

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
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 2
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 2

            # ESC를 누르면 게임이 종료하도록..
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
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
        if enemyX[i] < 0:
            enemyX_change[i] = -2
            # enemyY[i] += enemyY_change[i]
            # enemyY[i] += enemyY_change[i]

        # 살짝 억지 부려보았다.
        
        while enemyX[i] < -1:
            enemyX[i] = random.randint(300,800)
            #enemyY[i] = random.randint(0.600)
        
                # enemyY[i] += enemyY_change[i]   

        enemy(enemyX[i], enemyY[i], i)

    #enemyY += enemyY_change
    #if enemyY <= 0:
        #enemyY_change = 0.4

    #elif enemyY >= 550:
        #enemyY_change = -0.4
    
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

pygame.quit()

