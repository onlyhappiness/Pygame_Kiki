import pygame
from pygame import mixer
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

# Enemy 구현
enemyImg = [pygame.image.load('enemy/1.png') , pygame.image.load('enemy/2.png')]
#enemyImg = pygame.transform.scale(enemyImg, (110,130))
enemyMove = 0

# Background Sound
mixer.music.load('BGM.mp3')
mixer.music.play(-1)


# 폰트
font = pygame.font.Font('Goyang.ttf',35)

# 함수
def Message(size,mess,x_pos,y_pos):
    font = pygame.font.Font('Goyang.ttf',40)
    render = font.render(mess, True, white)
    screen.blit(render, (x_pos,y_pos))
    
def show_score(count):
    score = font.render("Score:" + str(count),True, white)
    screen.blit(score,(770,5))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x_random, y_random):
    global enemyMove

    if enemyMove + 1 >= 4:
        enemyMove = 0
        
    if y_random >= 0:
        screen.blit(enemyImg[enemyMove//2], (x_random, y_random))
        enemyMove += 1

"""
def enemy(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.init(self)

        #스피드
        self.speed = speed

        # 캐릭터 애니메이션
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Player 모든 이미지 로드
        animation_types = ['enemy']

        for animatino in animation_types:
            # 이미지 리스트 리셋
            temp_list = []

            # 폴더 안에 파일 들의 수를 카운트
            num_of_frames = len(os.listdir(f'enemy/{self.char_type}/{animation}'))

            # 캐릭터 움직임
            for i in range(num_of_framse):
                enemyImg = pygame.image.load(f'enemy/{self.char_type}/{animation}/{i}.png')
                enemyImg = pygame.trasnform.scale(enemyImg, int(enemyImg.get_width() * scale), int(enemyImg.get_height() * scale))
                temp_list.append(enemyImg)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
"""        

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
"""
def game_life(life,playerX,x_random,playerY,y_random):
    life = font.render("Life:" + str(life),True, white)
    screen.blit(life,(5,5))
    iscrash = False
"""

# 게임 루프
def Game_loop():
    playerX = 0
    playerY = 200
    playerX_change = 0
    playerY_change = 0

    x_random = 900
    y_random = random.randrange(0,600)

    count = 0
    life = 5

    iscrash = False
    
    running = True
    while running:
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

            # 키키 컨셉에 맞춰 비행을 능숙하지 않다는 점을 고려하여
            # 이동키를 누르지 않으면 플레이어가 멈추는 것을 주석처리...
            """
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    playerX_change = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    playerY_change = 0
            """

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
pygame.display.update()

pygame.quit()

