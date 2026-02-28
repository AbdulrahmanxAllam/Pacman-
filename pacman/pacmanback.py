import pygame

pygame.init()

SCREEN_WIDTH = 589
SCREEN_HEIGHT = 790
CELL_SIZE = 14
FPS = 15

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 105, 180)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

font = pygame.font.SysFont('Arial', 18)

# board image
board = [
    "####################  ####################", 
    "#******************#  #******************#", 
    "#* . . . . . . . .*#  #*. . . . . . . ..*#", 
    "#*.**************.*#  #*.**************.*#", 
    "#* *############* *#  #* *############* *#", 
    "#*o*#          #*.*#  #*.*#          #*o*#", 
    "#* *#          #* *#  #* *#          #* *#", 
    "#*.*############*.*####*.*############*.*#", 
    "#* ************** ****** ************** *#", 
    "#*. . . . . . . . . . . . . . . . . . ..*#",
    "#* ****** ***** ********** ***** ****** *#",
    "#*.*####*.*###*.*########*.*###*.*####*.*#",
    "#* *#  #* *# #* *#      #* *# #* *#  #* *#",
    "#*.*####*.*###*.*###  ###*.*###*.*####*.*#",
    "#* ****** ***** ***#  #*** ***** ****** *#",
    "#*. . . . . . . . *#  #*. . . . . . . ..*#",
    "#******** ******* *#  #* ******* ********#",
    "########*.*#####* *#  #* *#####*.*########",
    "       #* *#   #* *####* *#   #* *#       ", 
    "       #*.*#####* ****** *#####*.*#       ",
    "       #* ******* ****** ******* *#       ",
    "       #*.  . . . . . . . . . . .*#       ",
    "       #* *********     ******** *#       ",
    "########*.*########-----#######*.*########",
    "********* *#                  #* *********",
    "*********.*#                  #*.*********",
    "  . . . . *#                  #*  . . . . ", 
    "*********.*#                  #*.*********", 
    "********* *#                  #* *********",
    "########*.*####################*.*########",
    "       #* ********************** *#       ",
    "       #*.  . . . . . . . . . . .*#       ",
    "       #* ******* ****** ******* *#       ",
    "       #*.*#####* ****** *#####*.*#       ",
    "       #* *#   #* *####* *#   #* *#       ",
    "########*.*#####* *#  #* *#####*.*########",
    "#******** ******* *#  #* ******* ********#",
    "#*. . . . . . . . *#  #*. . . . . . . ..*#",
    "#* ****** *********#  #********* ****** *#",
    "#*.*####* *#########  #########* *####*.*#",
    "#* *#  #* *#                  #* *#  #* *#",
    "#*.*####* *####################*.*####*.*#",
    "#* ****** ********************** ****** *#",
    "#*  . . . . . . . . . . . . . . . . . ..*#",
    "#*.************** ****** **************.*#",
    "#* *############*.*####*.*############* *#",
    "#*.*#          #* *#  #* *#          #*.*#",
    "#* *#          #*.*#  #*.*#          #* *#",
    "#*o*############* *#  #* *############*o*#",
    "#* ************** *#  #* ************** *#",
    "#*.. . . . . . . .*#  #*. . . . . . . ..*#",
    "#******************#  #******************#",
    "####################  ####################", 
]

# Pac-Man and ghost images
pacman_img = pygame.image.load('Assets/ppac.jpg')
pacman_img = pygame.transform.scale(pacman_img, (CELL_SIZE * 2.5, CELL_SIZE * 2.5)) 

purple_ghost = pygame.image.load('Assets/pppurple.jpg')
purple_ghost = pygame.transform.scale(purple_ghost, (CELL_SIZE * 4, CELL_SIZE * 4))

red_ghost = pygame.image.load('Assets/red.png')
red_ghost = pygame.transform.scale(red_ghost, (CELL_SIZE * 4, CELL_SIZE * 4))

cyan_ghost = pygame.image.load('Assets/cyan.png')
cyan_ghost = pygame.transform.scale(cyan_ghost, (CELL_SIZE * 4, CELL_SIZE * 4))

green_ghost = pygame.image.load('Assets/green.png')
green_ghost = pygame.transform.scale(green_ghost, (CELL_SIZE * 4, CELL_SIZE * 4))

dead_ghost = pygame.image.load('Assets/dead.png')
dead_ghost = pygame.transform.scale(dead_ghost, (CELL_SIZE * 4, CELL_SIZE * 4))

cherry = pygame.image.load('Assets/cherry.jpg')
cherry = pygame.transform.scale(cherry, (CELL_SIZE*3, CELL_SIZE*3))

# Initialization and jobs
pacman_x, pacman_y = 20, 31
pacman_direction = 'RIGHT'
score = 0
lives = 3
ghosts = [
    {'x': 26.5, 'y': 26, 'image': purple_ghost, 'algorithm': 'A*', 'dead': False, 'dead_timer': 0},
    {'x': 22, 'y': 26, 'image': red_ghost, 'algorithm': 'BFS', 'dead': False, 'dead_timer': 0},
    {'x': 17.5, 'y': 26, 'image': cyan_ghost, 'algorithm': 'DFS', 'dead': False, 'dead_timer': 0},
    {'x': 13, 'y': 26, 'image': green_ghost, 'algorithm': 'UCS', 'dead': False, 'dead_timer': 0},
] #3ala hasab anhy ghost ento hat2asemo 8ayaro el esm ex 'a*' L esm el function aw algorithm youll use  
#MATEL3ABOSH FEL NUMBERS 3ALASHAN DOL EL STSRTING POINTS 


#board drawing function
def draw_board():
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(screen, PINK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == '*':  
                pygame.draw.rect(screen, 'black', (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE//10, CELL_SIZE//10))
            elif cell == '.':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 4)
            elif cell == 'o':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 9)

# Score panel
def draw_score_panel():
    pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, SCREEN_HEIGHT - 40))
    
    # Draw lives (cherry icons)
    for i in range(lives):
        screen.blit(cherry, (150 + i * 20, SCREEN_HEIGHT - 45))

#pacman 
def draw_pacman():
    if pacman_direction == 'LEFT':
        rotated_image = pygame.transform.rotate(pacman_img, 180)
    elif pacman_direction == 'RIGHT':
        rotated_image = pacman_img  
    elif pacman_direction == 'UP':
        rotated_image = pygame.transform.rotate(pacman_img, 90)
    elif pacman_direction == 'DOWN':
        rotated_image = pygame.transform.rotate(pacman_img, -90)
    screen.blit(rotated_image, (pacman_x * CELL_SIZE - rotated_image.get_width() // 2, pacman_y * CELL_SIZE - rotated_image.get_height() // 2))


#ghosts
def draw_ghosts():
    for ghost in ghosts:
        if ghost['dead']:
            screen.blit(dead_ghost, (ghost['x'] * CELL_SIZE - CELL_SIZE // 2, ghost['y'] * CELL_SIZE - CELL_SIZE // 2))
        else:
            screen.blit(ghost['image'], (ghost['x'] * CELL_SIZE - CELL_SIZE // 2, ghost['y'] * CELL_SIZE - CELL_SIZE // 2))

# function for the dead ghosts 
def dead_ghosts():
    current_time = pygame.time.get_ticks() #in ms
    for ghost in ghosts:
        if ghost['dead'] and current_time - ghost['dead_timer'] > 5000:  # 5 seconds dead time
            #revive w return to normal
            ghost['dead'] = False  
            if ghost['image'] == dead_ghost:
                if ghost == ghosts[0]:
                    ghost['image'] = purple_ghost
                elif ghost == ghosts[1]:
                    ghost['image'] = red_ghost
                elif ghost == ghosts[2]:
                    ghost['image'] = cyan_ghost
                elif ghost == ghosts[3]:
                    ghost['image'] = green_ghost

#movement for pacman dont touch pls 
def move_pacman():
    global pacman_x, pacman_y, score

    if pacman_direction == 'LEFT':
        if pacman_x > 0 and board[pacman_y][pacman_x - 1] not in ['#', '*']: 
            pacman_x -= 1
        
        elif pacman_x == 0 and board[pacman_y][len(board[0]) - 2] not in ['#', '*']:
            pacman_x = len(board[0]) - 2  

    elif pacman_direction == 'RIGHT':
        if pacman_x < len(board[0]) - 2 and board[pacman_y][pacman_x + 1] not in ['#', '*']:  
            pacman_x += 1
        
        elif pacman_x == len(board[0]) - 2 and board[pacman_y][0] not in ['#', '*']:
            pacman_x = 1  

    elif pacman_direction == 'UP' and pacman_y > 0 and board[pacman_y - 1][pacman_x] not in ['#', '*']:
        pacman_y -= 1
    elif pacman_direction == 'DOWN' and pacman_y < len(board) - 1 and board[pacman_y + 1][pacman_x] not in ['#', '*']:
        pacman_y += 1

    # Pac-Man eats a pellet
    if board[pacman_y][pacman_x] == '.':
        board[pacman_y] = board[pacman_y][:pacman_x] + ' ' + board[pacman_y][pacman_x + 1:]
        score += 10
    elif board[pacman_y][pacman_x] == 'o':
        board[pacman_y] = board[pacman_y][:pacman_x] + ' ' + board[pacman_y][pacman_x + 1:]
        score += 50
        
        #FORDEAD GHOSTS 
        for ghost in ghosts:
            ghost['dead'] = True
            ghost['dead_timer'] = pygame.time.get_ticks() 

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    draw_board()
    draw_pacman()
    draw_ghosts()
    draw_score_panel()
    dead_ghosts()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                pacman_direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                pacman_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                pacman_direction = 'DOWN'
    
    move_pacman()
    
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

pygame.quit()