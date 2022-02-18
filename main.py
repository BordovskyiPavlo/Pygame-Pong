import pygame , random , time
pygame.init()
pygame.display.set_caption("ping_pong")
online = True
bot_racket = []
size = 5
color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (255, 255, 0)
clock = pygame.time.Clock()
score = 0
balls_move = (random.randint(-1, 1), random.randint(-1, 1))
font = pygame.font.SysFont('serif', 25)
text1 = font.render("Score: " + str(score), True, color1)
class ping_pong:
    def create_area(self,height, width):
        self.gamescreen = pygame.display.set_mode((height,width))
        self.background = pygame.Surface((height,width))
        self.background.fill((0,0,0))
    def create_player(self,cord_x,cord_y):
        # player start x = 35 player start y = 250
        # up wall 500 , down wall 0
        self.cube = pygame.Surface((25,100))
        self.cube.fill(color1)
        self.player_racket = self.cube.get_rect()
        self.player_racket.move_ip(35, 250)
        self.gamescreen.blit(self.cube, self.player_racket)
        pygame.display.update()
    def create_ball(self, cord_x, cord_y):
        self.balls = pygame.Rect(cord_x, cord_y, 25, 25)
        pygame.draw.rect(self.gamescreen, color3, self.balls)
    def ball_move(self, cord_x, cord_y):
        pygame.Rect.move(self.balls, cord_x, cord_y)
        pygame.display.flip()
    def create_bot(self,cord_x,cord_y):
        # bot start x = 740 bot start y = 250
        self.cube2 = pygame.Surface((25, 100))
        self.cube2.fill(color2)
        self.bot_racket = self.cube2.get_rect()
        self.bot_racket.move_ip(740, 250)
        self.gamescreen.blit(self.cube2, self.bot_racket)
        pygame.display.update()
    def bot_move(self,x,y):
        self.bmin_y = 250
        self.bmax_y = 350
        if y >self.bot_racket[1]:
            self.bot_racket.move_ip(0, 1)
        if y <self.bot_racket[1]:
            self.bot_racket.move_ip(0, -1)
        if self.bot_racket[1] >= 500:
            self.bot_racket.move_ip(0, 0)
        if self.bot_racket[1] <= 0:
            self.bot_racket.move_ip(0, 0)

        self.gamescreen.blit(self.cube2, self.bot_racket)
        pygame.display.update()
    def player_move(self,cord_x,cord_y):
        self.player_racket.move_ip(cord_x,cord_y)
        self.gamescreen.blit(self.cube, self.player_racket)
        self.x = self.balls[0]
        self.y = self.balls[1]
        pygame.display.update()
    def update_screen(self,ball_cord_x,ball_cord_y):
        self.gamescreen.blit(self.background, (0, 0))
        self.gamescreen.blit(self.cube, self.player_racket)
        self.gamescreen.blit(self.cube2, self.bot_racket)
        self.gamescreen.blit(text1, (100, 100))
        pygame.draw.rect(self.gamescreen, color3, (ball_cord_x, ball_cord_y, 25, 25))
if __name__ =='__main__':
    player_cord_x = 35
    bot_cord_x = 740
    player_cord_y = 250
    bot_cord_y = 250
    ball_x = 350
    ball_y = 250
    ball = (ball_x, ball_y)
    K_w = pygame.K_w
    K_s = pygame.K_s
    p = ping_pong()
    p.create_area(800, 600)
    p.create_player(player_cord_x, player_cord_y)
    p.create_bot(bot_cord_x, bot_cord_y)
    p.create_ball(350,250)
    pmin_y = 250
    pmax_y = 350
    bmin_y = 250
    bmax_y = 350
    while online:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                online = False
        clock.tick(160)
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            if  player_cord_y<= 0:
                p.player_move(0, 0)
                pygame.display.update()
            elif player_cord_y > 0:
                player_cord_y+= -1
                p.player_move(0, -1)
                pmin_y += -1
                pmax_y +=  -1
                pygame.display.update()
        elif keys[K_s]:
            if player_cord_y >= 500:
                p.player_move(0, 0)
                pygame.display.update()
            elif player_cord_y < 500:
                player_cord_y += 1
                p.player_move(0, 1)
                pmin_y += 1
                pmax_y += 1
                pygame.display.update()
        pygame.display.flip()
        p.update_screen(ball_x,ball_y)
        if ball_y >= 580:  # down wall
            if balls_move == (0, 1):
                balls_move = (0, -1)
            if balls_move == (1, 1):
                balls_move = (1, -1)
            if balls_move == (-1, 1):
                balls_move = (-1, -1)
        if ball_y <= 0:  # up wall
            if balls_move == (-1, -1):
                balls_move = (-1, 1)
            if balls_move == (0, -1):
                balls_move = (0, 1)
            if balls_move == (1, -1):
                balls_move = (1, 1)
        if ball_x <= 60:
            if pmin_y<=ball_y <=pmax_y:
                if balls_move == (-1,0):
                    balls_move = (1,0)
                if balls_move == (-1, 1):
                    balls_move = (1, 1)
                if balls_move == (-1, -1):
                    balls_move = (1, -1)
        print(bmin_y,bmax_y)
        if ball_x >= 720:
            if bmin_y<=ball_y <=bmax_y:
                if balls_move == (1,1):
                    balls_move = (-1,1)
                if balls_move == (1, -1):
                    balls_move = (-1, -1)
                if balls_move == (1, 0):
                    balls_move = (-1, 0)
        ball_x += balls_move[0]
        ball_y += balls_move[1]
        bmin_y += balls_move[1]
        bmax_y += balls_move[1]
        print('ball:',ball_x,ball_y ,'\n','min , max :', bmin_y,bmax_y )
        p.bot_move(ball_x,ball_y)
        p.ball_move(balls_move[0],balls_move[1])
        pygame.display.update()