import pygame , random , time
pygame.init()
pygame.display.set_caption("ping_pong")
online = True
player_racket = []
bot_racket = []
size = 5
color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (255, 255, 0)
clock = pygame.time.Clock()
class ping_pong:
    def create_area(self,height, width):
        self.gamescreen = pygame.display.set_mode((height,width))
        self.background = pygame.Surface((height,width))
        self.background.fill((0,0,0))
    def create_player(self,cord_x,cord_y):
        # player start x = 35 player start y = 250
        player_racket=[(cord_x,cord_y)]
        pygame.draw.rect(self.gamescreen, color1, (cord_x,cord_y,25,100))
    def create_bot(self,cord_x,cord_y):
        # bot start x = 740 bot start y = 250
        pygame.draw.rect(self.gamescreen, color2, (740, 250, 25, 100))
    def player_move(self,cord_x,cord_y):
        #up wall 500 , down wall 0
        pygame.draw.rect(self.gamescreen, color1, (cord_x, cord_y, 25, 100))
        pygame.display.flip()
    def create_ball(self,cord_x,cord_y):
        pygame.draw.rect(self.gamescreen, color3, (cord_x, cord_y, 25, 25))
    def ball_move(self,cord_x,cord_y):
        pygame.draw.rect(self.gamescreen, color3, (cord_x, cord_y, 25, 25))
        pygame.display.flip()
        print(cord_x,cord_y)
    def update_screen(self,player_cord_x,player_cord_y,ball_cord_x,ball_cord_y):
        self.gamescreen.blit(self.background, (0, 0))
        pygame.draw.rect(self.gamescreen, color1, (player_cord_x, player_cord_y, 25, 100))
        pygame.draw.rect(self.gamescreen, color3, (ball_cord_x, ball_cord_y, 25, 25))
if __name__ =='__main__':
    player_cord_x = 35
    bot_cord_x = 740
    player_cord_y = 250
    bot_cord_y = 250
    ball_x = 350
    ball_y = 250
    ball = (ball_x,ball_y)
    K_w = pygame.K_w
    K_s = pygame.K_s
    p = ping_pong()
    p.create_area(800, 600)
    p.create_player(player_cord_x, player_cord_y)
    p.create_bot(bot_cord_x, bot_cord_y)
    p.create_ball(350,250)
    p.player_move(35, 250)
    x = int(random.randrange(-1, 2))
    y = int(random.randrange(-1, 2))
    balls_move = (x, y)
    if balls_move == (0, 0):
        x = int(random.randrange(-1, 2))
        y = int(random.randrange(-1, 2))
    balls_move = (x, y)
    while online:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                online = False
        clock.tick(50)
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            if player_cord_y <= 0:
                move = (0,0)
            elif player_cord_y > 0:
                move = (0, -5)
            player_cord_y += move[1]
            player_racket = [(player_cord_x, player_cord_y)]
            p.player_move(player_cord_x, player_cord_y)
        elif keys[K_s]:
            if player_cord_y >= 500:
                move = (0, 0)
            elif player_cord_y < 500:
                move = (0, 5)
            player_cord_y += move[1]
            player_racket = [(player_cord_x, player_cord_y)]
            p.player_move(player_cord_x, player_cord_y)
        p.update_screen(player_cord_x, player_cord_y, ball_x,ball_y)
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
        ball_x += balls_move[0]
        ball_y += balls_move[1]
        p.ball_move(ball_x,ball_y)
        pygame.display.update()