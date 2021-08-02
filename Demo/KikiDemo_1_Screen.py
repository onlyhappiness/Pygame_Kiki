import pygame

# pygame 초기화
pygame.init()

# 게임 화면 구현
screen = pygame.display.set_mode((800, 600))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
