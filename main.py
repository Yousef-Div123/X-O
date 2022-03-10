import pygame
import numpy as np
import random


row_count = 3
column_count = 3
gray = (200, 200, 200)
board = np.zeros((column_count, row_count))
turn = [1, 2, 1, 2, 1, 2, 1, 2, 1]
red=(200, 0, 0)
h_red=(255, 0, 0)
green = (0, 200, 0)
h_green = (0, 255, 0)
places = 0
squares = []
valid_location = []
squares = []
turn_count = 0
score_one = 0
score_two = 0
run_ai= False
run = False
play_menu_loop = False


#classes
#square
class square(object):
    def __init__(self, x, y, square_size, color, win, c, r):
        self.x = x 
        self.y = y
        self.square_size = square_size
        self.color = color
        self.c = c
        self.r = r
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.square_size, self.square_size))
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.square_size, self.square_size), 5)

#button
class button(object):
    def __init__(self, msg, x, y, t_width, width, height, color, h_color, action, menu):
        self.msg = msg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.h_color = h_color
        self.action = action
        self.menu = menu
        self.font_small = pygame.font.SysFont("comicsans", t_width )
        self.text_msg = self.font_small.render(self.msg, 1, (0, 0, 0))

    def draw(self, win):
        # button
        global menu_loop
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        global run
        global column_count
        global row_count
        global board
        global turn_count   
        global score_one
        global score_two
        global valid_location
        global run_ai
        global places
        global squares
        global play_menu_loop
        global play_menu
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(win, self.h_color, ( self.x, self.y, self.width, self.height))
            win.blit(self.text_msg, (self.x + 1, self.y + 3))
            if click[0] == 1:
                if self.action == "ai_easy":
                    ai_easy()
                elif self.action == "single_player":
                    single_player()    
                elif self.action == "play_menu":
                    play_menu()     
                elif self.action == "quit":
                    pygame.quit()
                    quit()
                elif self.action == "back":
                    menu()
                    run_ai =False
                    run = False
                    play_menu_loop = False
                    valid_location = []
                    turn_count = 0
                    board = np.zeros((column_count, row_count))
                    places = 0
                    squares = []
                    valid_location = []
                    squares = []
                    turn_count = 0
                    score_one = 0
                    score_two = 0 
                elif self.action == "back_play":
                    play_menu()
                    run_ai =False
                    run = False
                    valid_location = []
                    turn_count = 0
                    board = np.zeros((column_count, row_count))
                    places = 0
                    squares = []
                    valid_location = []
                    squares = []
                    turn_count = 0
                    score_one = 0
                    score_two = 0            
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height)) 
            win.blit(self.text_msg, (self.x + 1, self.y + 3))

def winning(board, piece):
    # horizantle
    for c in range(column_count):
        if board[c,0]==piece and board[c,1] == piece and board[c,2] == piece:
            return True     
    # vertical
    for r in range(row_count):
        if board[0,r]==piece and board[1,r] == piece and board[2,r] == piece:
            return True
    # postive line slope
    if board[0,2]==piece and board[1,1] == piece and board[2,0] == piece:
        return True
    # negative line slope
    if board[0,0]==piece and board[1,1] == piece and board[2,2] == piece:
        return True

def draw_board(board):
    pass

def menu():
    global win
    global run
    global run_ai
    global menu_loop
    global play_menu_loop
    menu_loop = True
    play_menu_loop = False
    run = False
    run_ai = False
    while menu_loop:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.fill((0, 200, 200))
        if menu_loop == True:
            #buttons
            font_name = pygame.font.SysFont("comicsans", 300, True)
            text_name = font_name.render("X-O", 1, (255, 0, 0))
            win.blit(text_name, (100, 120))
            quit_button = button("Quit", 100, 400, 100, 160, 100, red, h_red, "quit", menu)
            play_button = button("Play", 350, 400, 110, 160, 100, green, h_green, "play_menu", menu)
            quit_button.draw(win)
            play_button.draw(win)
            pygame.display.update()

def play_menu():
    global win
    global run
    global run_ai
    global menu_loop
    global play_menu
    menu_loop = False
    run = False
    run_ai = False
    play_menu_loop = True
    while play_menu_loop:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(play_menu_image, (0, 0))
        if play_menu_loop == True:
            #buttons
            ai_easy_button = button("Easy", 70, 210, 110, 180, 80, green, h_green, "ai_easy", menu)
            ai_easy_button.draw(win)
            single_player_button = button("Play", 60, 550, 110, 160, 80, (0, 0, 200), (0, 0, 255), "single_player", menu)
            single_player_button.draw(win)
            back_button = button("back", 400, 610, 100, 155, 80, (0, 145, 0), (0, 200, 0), "back", menu)
            back_button.draw(win)
            pygame.display.update()


pygame.init()
square_size = 200
win = pygame.display.set_mode((600, 700))
pygame.display.set_caption("x-o")
play_menu_image = pygame.image.load("play_menu.jpg")

def draw_screen(column_count, row_count):
    global win
    for c in range(column_count):
        for r in range(row_count):
            squares.append(square(r*square_size, c*square_size, square_size, gray, win, c, r))
        for s in squares:
            s.draw()
    pygame.draw.rect(win, (0, 0, 0), (0, 600, 600, 100))

def draw_squares(s):
    for s in squares:
        s.draw()
    pygame.draw.rect(win, (0, 0, 0), (0, 600, 600, 100))

def single_player():
    global win
    global green
    global h_green
    global menu
    global squares
    global square_size
    global square
    global button
    global turn_count
    global turn
    global score_two
    global score_one
    global run
    global menu_loop
    global run_ai
    global row_count
    global column_count
    global play_menu_loop

    board = np.zeros((column_count, row_count))
    run_ai = False
    run=True
    menu_loop = False
    play_menu_loop = False
    places = 0
    score_one = 0
    score_two = 0 
    turn = [1, 2, 1, 2, 1, 2, 1, 2, 1] 
    turn_count =0
    squares = []
    valid_location = []
    squares = []
    pygame.display.update()
    draw_board(board)
    draw_screen(column_count, row_count)
    draw_squares(squares)
    while run:
        pygame.time.delay(100)
        pygame.draw.rect(win, (0, 0, 0), (0, 600, 600, 100))    
        back_button = button("back", 10, 610, 100, 155, 80, green, h_green, "back_play", menu)
        back_button.draw(win)
        font_score = pygame.font.SysFont("comicsans", 50, True)
        text_score_one = font_score.render(str(score_one)+"  :player_1", 1, (0, 255, 0))
        text_score_two = font_score.render(str(score_two)+"  :player_2", 1, (0, 255, 0))
        win.blit(text_score_one, (350, 620))
        win.blit(text_score_two, (350, 660))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if menu_loop != True:
                if run_ai == False and play_menu_loop == False:    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        draw_board(board)
                        mx, my = pygame.mouse.get_pos()
                        valid_location=[]    
                        for s in squares:
                            if board[s.c, s.r] == 0 :
                                valid_location.append(s)
                        for s in valid_location:
                            if mx > s.x and mx < s.x+s.square_size:
                                if my > s.y and my < s.y+square_size:
                                    if turn[turn_count] == 1:
                                        places += 1
                                        pygame.draw.line(win, (0, 0, 0), (s.x + 20, s.y + 20), (s.x + 180, s.y + 180), 5)
                                        pygame.draw.line(win, (0, 0, 0), (s.x + 180, s.y + 20), (s.x + 20, s.y + 180), 5)
                                        turn_count += 1
                                        board[s.c, s.r]=1
                                        if winning(board, 1):
                                            font_win = pygame.font.SysFont("comicsans", 100, True)
                                            text_win1 = font_win.render("player_1 wins!!", 1, (255, 0, 0))
                                            win.blit(text_win1, (2, 250))
                                            pygame.display.update()
                                            pygame.time.delay(2000)
                                            turn_count = 0
                                            board = np.zeros((column_count, row_count))
                                            places = 0
                                            score_one += 1
                                            draw_squares(squares)
                                            valid_location = []

                                    else:
                                        places += 1
                                        pygame.draw.circle(win, (0, 200, 0), (s.x + 100, s.y + 100), 70, 5)    
                                        turn_count += 1
                                        board[s.c, s.r]=2
                                        if winning(board, 2):
                                            font_win = pygame.font.SysFont("comicsans", 100, True)
                                            text_win2 = font_win.render("player_2 wins!!", 1, (0, 0, 255))
                                            win.blit(text_win2, (2, 250))                                    
                                            pygame.display.update()
                                            pygame.time.delay(2000)
                                            turn_count = 0
                                            board = np.zeros((column_count, row_count))
                                            score_two +=1
                                            places = 0
                                            valid_location = []
                                            draw_squares(squares)
        if places >= 9:
            font_win = pygame.font.SysFont("comicsans", 100, True)
            text_draw = font_win.render("Draw!!", 1, (255, 0, 255))
            win.blit(text_draw, (100, 250))
            pygame.display.update()
            pygame.time.delay(2000)
            turn_count = 0
            board = np.zeros((column_count, row_count))
            places = 0
            draw_squares(squares)
            valid_location = []

        pygame.display.update()        
        
    
def ai_easy():
    global win
    global green
    global h_green
    global menu
    global valid_location
    global board
    global turn_count
    global turn
    global score_two
    global score_one
    global squares
    global square_size
    global square
    global button
    global run_ai
    global menu_loop
    global row_count
    global column_count
    global play_menu_loop

    board = np.zeros((column_count, row_count))

    run_ai=True
    menu_loop = False
    play_menu_loop = False
    valid_location = []
    places = 0
    score_one = 0
    score_two = 0 
    turn = [1, 2, 1, 2, 1, 2, 1, 2, 1] 
    turn_count =0
    squares = []
    valid_location = []
    squares = []
    pygame.display.update()
    draw_board(board)
    draw_screen(column_count, row_count)
    draw_squares(squares) 
    while run_ai:
        pygame.time.delay(100)
        pygame.draw.rect(win, (0, 0, 0), (0, 600, 600, 100))    
        back_button = button("back", 10, 610, 100, 155, 80, green, h_green, "back_play", menu)
        back_button.draw(win)
        font_score = pygame.font.SysFont("comicsans", 50, True)
        text_score_one = font_score.render(str(score_one)+"  :player_1", 1, (0, 255, 0))
        text_score_two = font_score.render(str(score_two)+"  :player_2", 1, (0, 255, 0))
        win.blit(text_score_one, (350, 620))
        win.blit(text_score_two, (350, 660))                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if menu_loop != True:
                if run ==False and play_menu_loop == False:    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        draw_board(board)
                        mx, my = pygame.mouse.get_pos()
                        valid_location = []
                        for s in squares:
                            if board[s.c, s.r] == 0 :
                                valid_location.append(s)
                        for s in valid_location:
                            if mx > s.x and mx < s.x+s.square_size:
                                if my > s.y and my < s.y+square_size:
                                    if turn[turn_count] == 1:
                                        places += 1
                                        pygame.draw.line(win, (0, 0, 0), (s.x + 20, s.y + 20), (s.x + 180, s.y + 180), 5)
                                        pygame.draw.line(win, (0, 0, 0), (s.x + 180, s.y + 20), (s.x + 20, s.y + 180), 5)
                                        turn_count += 1
                                        board[s.c, s.r]=1
                                        
                                        if winning(board, 1):
                                            valid_location = []
                                            font_win = pygame.font.SysFont("comicsans", 100, True)
                                            text_win1 = font_win.render("player_1 wins!!", 1, (255, 0, 0))
                                            win.blit(text_win1, (2, 250))
                                            pygame.display.update()
                                            pygame.time.delay(2000)
                                            turn_count = 0
                                            board = np.zeros((column_count, row_count))
                                            places = 0
                                            score_one += 1
                                            draw_squares(squares)
                if places < 9:                            
                    valid_location=[]    
                    for s in squares:
                        if board[s.c, s.r] == 0 :
                            valid_location.append(s)
                    if turn[turn_count] == 2:
                        pygame.time.wait(50)
                        s = random.choice(valid_location)
                        places += 1
                        pygame.draw.circle(win, (0, 200, 0), (s.x + 100, s.y + 100), 70, 5)    
                        turn_count += 1
                        board[s.c, s.r]= 2
                        if winning(board, 2):
                            valid_location = []
                            font_win = pygame.font.SysFont("comicsans", 100, True)
                            text_win2 = font_win.render("player_2 wins!!", 1, (0, 0, 255))
                            win.blit(text_win2, (2, 250))                                    
                            pygame.display.update()
                            pygame.time.delay(2000)
                            turn_count = 0
                            board = np.zeros((column_count, row_count))
                            score_two +=1
                            places = 0
                            draw_squares(squares)
        if places >= 9:
            font_win = pygame.font.SysFont("comicsans", 100, True)
            text_draw = font_win.render("Draw!!", 1, (255, 0, 255))
            win.blit(text_draw, (100, 250))
            pygame.display.update()
            pygame.time.delay(2000)
            turn_count = 0
            board = np.zeros((column_count, row_count))
            places = 0
            draw_squares(squares)    
        for s in squares:
            if board[s.c, s.r] == 0 :
                valid_location.append(s)
        pygame.display.update()        
                
menu()
