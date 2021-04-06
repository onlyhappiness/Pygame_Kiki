import pygame

# pygame 초기화
pygame.init()

# 게임 화면 구현
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Kiki's Delivery Service")
icon = pygame.image.load('witch.png')
pygame.display.set_icon(icon)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 
    screen.fill((0,51,255))
    pygame.display.update()
