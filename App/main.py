import pygame

# 무조건 해야됨
# TODO: 파이게임 초기화 
pygame.init()

# TODO: screen 생성
# FIXME: 크기는 다시 생각해보는 거로 ㄱㄱ
screen = pygame.display.set_mode((1280, 720))

# TODO: Caption and Icon
# pygame.display.set_caption('')
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)

# TODO: Player
playerImg = pygame.image.load('App/image/Kiki.png')
playerX = 370
playerY = 480

# TODO: 캐릭터 이동
playerX_change = 0
playerY_change = 0


def player(x, y):
  screen.blit(playerImg, (x, y))

# 게임 실행 = true
# TODO: Game Loop
running = True
while running:
  # RGB 색
  # screen.fill((0,0,0))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # TODO: 키 이벤트
    if event.type == pygame.KEYDOWN:
      print('Key pressed')
      if event.key == pygame.K_LEFT:
        print('Left arrow is pressed')
      if event.key == pygame.K_RIGHT:
        print('Right arrow is pressed')

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        print('Keystoke has been released')

  player(playerX, playerY)
  pygame.display.update()