from tkinter.tix import WINDOW
import pygame, sys

# TODO: 이건 뭐야?
clock = pygame.time.Clock()

# TODO: 파이게임 초기화 
pygame.init()

pygame.display.set_caption('pygame window')

# TODO: screen 생성 및 크기 조절
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# TODO: Player 이미지
player_image = pygame.image.load('App/image/Kiki.png')

# TODO: 움직임
moving_left = False
moving_right = False

# TODO: player 기본 위치
player_location = [50, 50]
player_y_momentum = 0


# TODO: Game Loop
running = True
while running:
  screen.fill((146,244,255))

  screen.blit(player_image, player_location)

  # TODO:
  if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
    player_y_momentum = -player_y_momentum
  else:
    player_y_momentum += 0.2
  player_location[1] += player_y_momentum
  

  # TODO: 움직임이 있다면 실행함
  if moving_left == True:
    player_location[0] -= 4
  if moving_right == True:
    player_location[0] += 4

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    # TODO: 키 이벤트
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        moving_left = True
      if event.key == pygame.K_RIGHT:
        moving_right = True
  
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        moving_left = False
      if event.key == pygame.K_RIGHT:
        moving_right = False
  
  pygame.display.update()
  clock.tick(60)