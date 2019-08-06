import pygame
import random
import sys


FPS = 10
HEIGHT = 450
WIDTH = 450
#====================================================================
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
#====================================================================

class TicTac:
    def __init__(self):
        # initialize all data of game
        pygame.init()
        self.clock = pygame.time.Clock()
        self._data = [0]*9
        self.turn = 0
        self.gameExit = False
        self.first_player = "You"
        self.second_player = "Computer"
        self.display = pygame.display
        self.gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
        self.draw_board()

    def update_data(self,pos,master):
        # updte the data of game
        if self._data[pos]==0:
            self._data[pos] = master
            return True
        return False

    def master_data(self,master):
        # return data for specific players
        return [k+1 for k in range(0,9) if self._data[k]==master]

    def draw_board(self):
        # draw the board with color
        self.gameDisplay.fill(WHITE)
        self.display.set_caption("Tic Tac Toe")
        x,y = 0,0
        for i in range(3):
            x = 0
            for j in range(3):
                col = GREEN if (i+j)%2==0 else BLUE
                pygame.draw.rect(self.gameDisplay,col,[x,y,145,145])
                x += 150
            y += 150

    def message_to_screen(self,msg,col,size,t_x,t_y):
        # function to display msg to screen
        font = pygame.font.SysFont(None,size)
        text = font.render(msg,True,col)
        text_rect = text.get_rect()
        text_rect.center = (t_x,t_y)
        self.gameDisplay.blit(text,text_rect)

    def game_end(self):
        # checks if game has ended
        if self.turn>=9:
            return True
        return False

    def check_winner(self):
        # checks which player won the game
        winner = None
        win_set = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
        first_player = self.master_data(1)
        second_player = self.master_data(2)
        for x,y,z in win_set:
            if x in first_player and y in first_player and z in first_player:
                winner = self.first_player
            elif x in second_player and y in second_player and z in second_player:
                winner = self.second_player
        return winner

    def result(self,winner):
        # show result on the screen
        self.gameDisplay.fill(WHITE)
        msg1 = 'Winner is {}.'.format(winner)
        self.message_to_screen(msg1,RED,40,225,210)
        msg2 = 'Press C to continue or Q to quit.'
        self.message_to_screen(msg2,BLUE,25,225,250)
        pygame.display.update()
        again = True
        while again:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    again = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        again = False
                        self.restart()
                    if event.key == pygame.K_q:
                        again = False

    def computer_move(self):
        update = False
        while not update:
            pos = random.randint(0,8)
            update = self.update_data(pos,2)
        # calculate row and col from pos
        row = pos//3
        col = pos-3*(pos//3)
        self.message_to_screen('X',BLACK,50,75+(150*col),75+(150*row))
        self.turn += 1
                        

    def __events(self):
        # check for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                col,row = event.pos
                if(row<450 and col<450):
                    col,row = col//150,row//150
                    pos = col+row*3
                    updated = self.update_data(pos,1)
                    if updated:
                        self.message_to_screen('O',BLACK,50,75+(150*col),75+(150*row))
                        self.turn += 1

    def __update(self):
        # update data and screen
        if self.turn%2==1 and self.turn<9:
            self.computer_move()
        self.display.update()
        gameEnd = game.game_end()
        winner = game.check_winner()
        if gameEnd or (not winner is None):
            self.gameExit = True
            self.result(winner)
            
    def run(self):
        # run the game
        while not self.gameExit:
            self.clock.tick(FPS)
            self.__events()
            self.__update()
        # release pygame and exit out of game
        pygame.quit()
        sys.exit()
            

    def restart(self):
        # restarts the game
        self.__init__()


if __name__=='__main__':
    # create game object
    game = TicTac()
    game.run()
    
