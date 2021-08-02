import pygame
import random
import time

clock = pygame.time.Clock()

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
playerImg = pygame.transform.scale(playerImg, (180,150))

enemyImg = pygame.image.load('Raven.png') # Enemy 구현
enemyImg = pygame.transform.scale(enemyImg, (110,130))

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

def button(x_button, y_button, mess_b):
    pygame.draw.rect(screen, green, [x_button, y_button, 150, 50])
    Message(50, mess_b, x_button, y_button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x_button < mouse[0] < x_button + 100 and y_button < mouse[1] < y_button+30:
        pygame.draw.rect(screen, light_green, [x_button, y_button, 100, 30])
        Message(50, mess_b, x_button, y_button)
        if click == (1,0,0) and mess_b == "배달 시작!":
            Game_loop()
        elif click == (1,0,0) and mess_b == "나가기":
            pygame.quit()

def game_intro():
    intro = True
    while intro:
        screen.blit(intro_background, (0,0))
        button(100, 300, "배달 시작!")
        button(600, 300, "나가기")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        
        pygame.display.update()

# 까마귀랑 충돌
def bird_strike(playerX,x_random,playerY,y_random):
    if x_random-60 < playerX < x_random+60 and y_random-60 < playerY < y_random+60:
    
        Message(100, "조심해..!", 400, 300)
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
      
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

        player(playerX, playerY)
        enemy(x_random,y_random)
        x_random -= 4
        if x_random == 0:
            x_random = 900
            y_random = random.randrange(0,600)
            count += 1
        bird_strike(playerX,x_random,playerY,y_random)     
        show_score(count)
        pygame.display.update()

game_intro()
#Game_loop()
pygame.display.update()

pygame.quit()

