import pygame

# pygame 초기화
pygame.init()

# 게임 화면 구현 (노트북 화면과 호환되도록 하였음..)
screen = pygame.display.set_mode((900, 650))

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

def player(x,y):
    screen.blit(playerImg,(x,y))



# 게임 루프
running = True
while running:
    screen.fill((0,51,255))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키를 눌렀을 때 움직이는 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    # player가 화면 밖으로 나갈 경우
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
    pygame.display.update()

