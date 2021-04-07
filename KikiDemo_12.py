import pygame
import random
import time

#clock = pygame.time.Clock()

# pygame 초기화
pygame.init()

# 게임 화면 구현
# 15인치 화면에 호환되도록 하였기 때문에
# 다른 desktop에서 보면 작게 보일 수 있습니다...)
screen = pygame.display.set_mode((900, 650))

# color
green = (0,255,0)
white = (255, 255, 255)
light_green = (0,200,0)

# Title and Icon
pygame.display.set_caption("Kiki's Delivery Service")
icon = pygame.image.load('witch.png')
pygame.display.set_icon(icon)

# Image
background = pygame.image.load('background.jpg')
intro_background = pygame.image.load('intro.jpg')
playerImg = pygame.image.load('kiki.png') # Player 구현
enemyImg = pygame.image.load('Raven.png') # Enemy 구현

# 폰트
font = pygame.font.Font('Goyang.ttf',40)

# 함수
def Message(size,mess,x_pos,y_pos):
    render = font.render(mess, True, white)
    screen.blit(render, (x_pos,y_pos))
    
#Message(100,"START",150,100)
#clock.tick(1)

def show_score(count):
    score = font.render("Score:" + str(count),True, white)
    screen.blit(score,(10,10))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x_random, y_random):
    screen.blit(enemyImg, (x_random, y_random))

# 게임 루프
def Game_loop():
    playerX = 0
    playerY = 200
    playerX_change = 0
    playerY_change = 0

    x_random = 900
    y_random = random.randrange(0,600)

    count = 0
    textX = 10
    textY = 10
    
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
                    playerX_change = -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = 1
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    playerY_change = -1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    playerY_change = 1

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

    
        enemy(x_random,y_random)
        x_random -= 3
        if x_random == 0:
            x_random = 900
            y_random = random.randrange(0,600)
            count += 1
        player(playerX, playerY)
        show_score(count)
        pygame.display.update()

#game_intro()
Game_loop()
pygame.display.update()
pygame.quit()

