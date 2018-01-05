import pygame
import time

NAUGHT = 'O'
CROSS = 'X'
SIZE = 300
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

state = NAUGHT
board = {}
xPan = 7
yPan = -25

pygame.quit()
pygame.init()
gameDisplay = pygame.display.set_mode((SIZE,SIZE))
clock = pygame.time.Clock()
default_font = pygame.font.SysFont('comicsansms', 100)
gameover_font = pygame.font.SysFont('comicsansms', 30)

gameDisplay.fill(BLACK)
pygame.display.update()

def checkWinner(s):
    playerList = {key:value for key,value in board.items() if value == s}
    return ((0,0) in playerList and (1,0) in playerList and (2,0) in playerList) or \
       ((0,1) in playerList and (1,1) in playerList and (2,1) in playerList) or \
       ((0,2) in playerList and (1,2) in playerList and (2,2) in playerList) or \
       ((0,0) in playerList and (0,1) in playerList and (0,2) in playerList) or \
       ((1,0) in playerList and (1,1) in playerList and (1,2) in playerList) or \
       ((2,0) in playerList and (2,1) in playerList and (2,2) in playerList) or \
       ((0,0) in playerList and (1,1) in playerList and (2,2) in playerList) or \
       ((0,2) in playerList and (1,1) in playerList and (0,2) in playerList)

def gameOver():
    return checkWinner(NAUGHT) or checkWinner(CROSS) or len(board) == 9

while not gameOver():
    while True:
##      Check to quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
##      Get mouse position in 9x9 grid form
        for c in range(3):
            for r in range(3):
                if c * SIZE / 3 <= pygame.mouse.get_pos()[0] < (c + 1) * SIZE / 3 and r * SIZE / 3 <= pygame.mouse.get_pos()[1] < (r + 1) * SIZE / 3 :
                    pos = (c,r)
##      Display state if clicked
        if pygame.mouse.get_pressed()[0] == 1 and pos not in board:
            board[pos] = state
            gameDisplay.blit(default_font.render(state,1,WHITE), (pos[0] * SIZE / 3 + xPan, pos[1] * SIZE / 3 + yPan))
            break
##  Swap state
    if state == NAUGHT:
        state = CROSS
    else:
        state = NAUGHT
##  Update the surface
    pygame.display.update()
    clock.tick(1)
##Define Game Over Text
if checkWinner(NAUGHT):
    gameOverText = '!! NAUGHT WINS !!'
elif checkWinner(CROSS):
    gameOverText = '!! CROSS WINS !!'
else:
    gameOverText = 'GAME OVER'
##Display Game Over Text
gameDisplay.blit(gameover_font.render(gameOverText,1,GREEN), (0, SIZE / 2))
pygame.display.update()
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
