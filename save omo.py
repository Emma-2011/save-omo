import pygame,random
pygame.init( )

sc = pygame.display.set_mode((500,500))

pygame.display.set_caption("save omo")

gameover = pygame.image.load("C:\\mxcmaterials\\拯救omo-gameover-e4ac8b67-f4a1-45b2-8501-16045af0dd3f.png")
youwin = pygame.image.load("C:\\mxcmaterials\\拯救omo-youwin-aad8d2d6-62d9-4152-a57f-0087bc57a38a.png")
bg = pygame.image.load("C:\\mxcmaterials\\拯救omo-bg-a484bd70-e04b-4f9b-a2b0-391cfc147dc5.png")
omo_img =pygame.image.load("C:\\mxcmaterials\\拯救omo-omo-11239ff3-6d76-43fd-a0fd-5dfc67c10ff3.png")
boom_img = pygame.image.load("C:\\mxcmaterials\\拯救omo-boom-3e822671-f093-4f5b-a10c-be8d5b4f11a5.png")
star_img = pygame.image.load("C:\\mxcmaterials\\拯救omo-star-a0c7784e-8164-43be-babe-2910179b1327.png")
ghost_img = pygame.image.load("C:\\mxcmaterials\\拯救omo-ghost-2b17ecaa-f72b-409e-9e0f-0a26545768d8.png")
click_sound = pygame.mixer.Sound("C:\\mxcmaterials\\拯救omo-点击-ca25201f-206d-4182-9b18-0d70fbfab6d0.wav")
win_sound = pygame.mixer.Sound("C:\\mxcmaterials\\拯救omo-胜利-4b5c44f6-407c-4fa1-b2fd-e52cfea7e211.wav")
over_sound = pygame.mixer.Sound("C:\\mxcmaterials\\拯救omo-背景音乐-b2cac911-d110-45ba-91e8-369f6e3077df.wav")
star_sound = pygame.mixer.Sound("C:\\mxcmaterials\\拯救omo-获得星星-04958dde-b6f9-43f1-b8c8-d5aba526e798.wav")
# 播放背景音乐
pygame.mixer.music.load("C:\\mxcmaterials\\拯救omo-背景音乐-b2cac911-d110-45ba-91e8-369f6e3077df.wav")
pygame.mixer.music.play(loops=-1)

#omo 类的设计
class Omo:
    def __init__(self):
        self.x =random.randint(0,450)
        self.y = random.randint(0,450)
    def draw_me(self):
        sc.blit(omo_img,(self.x,self.y))
class Boom(Omo):
    def draw_me(self):
        sc.blit(boom_img,(self.x,self.y))
    def move(self):
        self.x += random.randint(-4,4)
        self.y += random.randint(-4,4)
class Ghost(Omo):
    def draw_me(self):
        sc.blit(ghost_img,(self.x,self.y))
    def move(self):
        self.x += random.randint(-4,4)
        self.y += random.randint(-4,4)
        
class Star:
    def __init__(self):
        self.x =random.randint(0,450)
        self.y = random.randint(-1000,-100)
    def draw_me(self):
        sc.blit(star_img,(self.x,self.y))
        self.move()
    def move(self):
        self.y+=1
        if self.y>500:
            self.reset()
    def reset(self):
        self.x =random.randint(0,450)
        self.y = random.randint(-1000,-100)
        
class GameTime:
    def __init__(self):
        self.set_time=10
        self.remain_time=0
        self.count_time=0
        self.start_time=pygame.time.get_ticks()
        
    def count_down(self):
        self.count_time = (pygame.time.get_ticks()-self.start_time)//1000
        
        self.remain_time =self.set_time - self.count_time
        
    def add_time(self):
        self.set_time +=10

def mouse_click():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        mouse_x,mouse_y=pygame.mouse.get_pos()
        for o in ghost_list:
            if o.x< mouse_x < o.x +50 and o.y< mouse_y < o.y +50:
                return "ghost"
        if event.type== pygame.MOUSEBUTTONDOWN:
            for o in boom_list:
                if o.x< mouse_x < o.x +50 and o.y< mouse_y < o.y +50:
                    return "boom"
            for o in omo_list:
                if o.x< mouse_x < o.x +50 and o.y< mouse_y < o.y +50:
                    omo_list.remove(o)
                    return "omo"
            o=real_omo
            if o.x< mouse_x < o.x +50 and o.y< mouse_y < o.y +50:
                return "win"
                
            if star.x < mouse_x < star.x + 50 and star.y < mouse_y < star.y + 50:
                star.reset()
                return "star"
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                omo_list.clear()
            if event.key == pygame.K_RIGHT:
                boom_list.clear()
omo_list=[]
boom_list=[]
ghost_list=[]
for i in range(9):
    omo=Omo()
    omo_list.append(omo)
real_omo =Omo()

for i in range(10):
    boom=Boom()
    boom_list.append(boom)

for i in range(10):
    ghost=Ghost()
    ghost_list.append(ghost)
star = Star()
game_time = GameTime()
font = pygame.font.SysFont("Cursive",48,True)
while True:
    sc.blit(bg,(0,0))
    game_time.count_down()
    time_text = font.render("TIME: "+str(game_time.remain_time),True,(255,0,0))
    sc.blit(time_text,(50,20))
    star.draw_me()
    for omo in omo_list:
        omo.draw_me()
    real_omo.draw_me()
    for boom in boom_list:
        boom.draw_me()
        boom.move()
    for ghost in ghost_list:
        ghost.draw_me()
        ghost.move()
    res = mouse_click()
    if res == "omo":
        click_sound.play()
    if res=="ghost" or res =="boom" or game_time.remain_time==0:
        sc.blit(bg,(0,0))
        sc.blit(gameover,(100,170))
        over_sound.play()
        pygame.mixer.music.stop()
        pygame.display.update()
        break
    if res == "win":
        sc.blit(bg,(0,0))
        sc.blit(youwin,(100,170))
        win_sound.play()
        pygame.mixer.music.stop()
        pygame.display.update()
        break
    if res =="star":
        star_sound.play()
        game_time.add_time()
    
    pygame.display.update()

input()
