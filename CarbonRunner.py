import pygame
import random
import math
from pygame.locals import *

pygame.init()

Width = 1500
Height = 500

clock = pygame.time.Clock()
FPS = 25

score = 0
high_score = 0

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Carbon Runner')

m = 0

def menu():
    global m
    # print("entered menu function")
    screen.fill('black')
    p = pygame.draw.rect(screen, 'orange', (Width//2 - 200, Height//2 - 50, 100, 50))
    q = pygame.draw.rect(screen, 'orange', (Width//2 + 100, Height//2 - 50, 100, 50))
    
    play_text = font.render("Play", True, 'white')
    play_text_rect = play_text.get_rect()
    play_text_rect.center = (p.center)

    quit_text = font.render("Quit", True, 'white')
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = (q.center)

    screen.blit(play_text, play_text_rect)
    screen.blit(quit_text, quit_text_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
            if p.collidepoint(event.pos):
                m = 1
                # print("m after play clicked", m)
            elif q.collidepoint(event.pos):
                pygame.quit()

def game_over():
    global m
    # print("entered menu function")
    screen.fill('black')
    p = pygame.draw.rect(screen, 'orange', (Width//2 - 200, Height//2 - 50, 100, 50))
    q = pygame.draw.rect(screen, 'orange', (Width//2 + 100, Height//2 - 50, 100, 50))

    game_over_text = font.render("Game Over!", True, 'red')
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (Width//2, Height//2 - 100)
    
    play_text = font.render("Play", True, 'white')
    play_text_rect = play_text.get_rect()
    play_text_rect.center = (p.center)

    quit_text = font.render("Quit", True, 'white')
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = (q.center)

    screen.blit(play_text, play_text_rect)
    screen.blit(quit_text, quit_text_rect)
    screen.blit(game_over_text, game_over_text_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
            if p.collidepoint(event.pos):
                m = 1
                # print("m after play clicked", m)
            elif q.collidepoint(event.pos):
                pygame.quit()

anime_run = []
anime_jump = []

bg = pygame.image.load("BG.png")

player_height = 0
is_jumping = False

font = pygame.font.Font("Ankh.ttf", 40)

carbon_text = font.render("Meter: ", True, (1, 50, 32))
carbon_rect = carbon_text.get_rect()
carbon_rect.topleft = (250, 10)

collect_sound = pygame.mixer.Sound("collect.wav")
loss_sound = pygame.mixer.Sound("loss.wav")

for i in range(0, 7, 2):
    image_name = "run__00" + str(i) + ".png"
    player_image = pygame.image.load(image_name)
    player_rect = player_image.get_rect()
    player_rect.centerx = Width//2
    player_rect.y = player_height = Height - player_image.get_height()
    anime_run.append(player_image)

for i in range(0, 7, 2):
    image_name = "jump__00" + str(i) + ".png"
    player_image = pygame.image.load(image_name)
    player_rect = player_image.get_rect()
    player_rect.centerx = Width//2
    player_rect.y = player_height = Height - player_image.get_height()
    anime_jump.append(player_image)

num_collectables = 100

class Collectable(pygame.sprite.Sprite):
    def __init__(self, image_name, score_boost, footprint, isgood):
        super().__init__()
        self.image_name = image_name
        self.score_boost = score_boost
        self.footprint = footprint
        self.isgood = isgood
        self.rect = None

collectables = []

def initCollectables():
    global collectables
    collectables = []
    for i in range(num_collectables):
        chance = random.randint(1, 100)
        if chance <= 25:
            leaf = Collectable("leaf1.png", 2, -20, True)
            collectables.append(leaf)
        elif chance <= 45:
            panel = Collectable("panel1.png", 5, -30, True)
            collectables.append(panel)
        elif chance <= 60:
            evbattery = Collectable("evbattery.png", 10, -40, True)
            collectables.append(evbattery)
        elif chance <= 100:
            smog_cloud = Collectable("smog_cloud.png", 0, 20, False)
            collectables.append(smog_cloud)

    space = random.randint(50, 125)

    for i in range(len(collectables)):
        collect_image = pygame.image.load(collectables[i].image_name)
        collectables[i].rect = collect_image.get_rect()
        collectables[i].rect.x = Width + space
        collectables[i].rect.y = Height - collect_image.get_height()
        space += random.randint(350, 650)

initCollectables()

bg_width = bg.get_width()
tiles = math.ceil(Width / bg_width) + 1

scroll = 0
count = 0
jump_count = 0
y_velocity = 0
jump_velocity = -15
gravity = 0.9

meter_length = 20

line = 1

pygame.mixer.music.load("Song.wav")

pygame.mixer.music.play(-1, 0.0)

score_boost_text = font.render("", True, (1, 50, 32))
score_boost_rect = score_boost_text.get_rect()
score_boost_rect.bottomleft = (player_rect.topleft)

boost_distance = 75

color = 'green'

while True:

    clock.tick(FPS)

    if m == 0:
        menu()
        pygame.display.update()
    elif m == 2:
        game_over()
        pygame.display.update()
    elif m == 1:

        count += 1

        if collectables[num_collectables - 1].rect.x < 0:
            initCollectables()

        #Update Score
        score_text = font.render("Score: " + str(score), True, (0, 0, 139))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)
        high_score_text = font.render("High Score: " + str(high_score), True, (0, 0, 139))
        high_score_rect = high_score_text.get_rect()
        high_score_rect.topleft = (1200, 10)

        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll - (i * line), 0))

        carbon = pygame.draw.rect(screen, color, (420, 29, meter_length, 10))
        pygame.draw.rect(screen, (139, 0, 0), (420, 29, 150, 10), 1)

        if meter_length <= 50:
            color = 'green'
        elif meter_length <= 100:
            color = 'orange'
        elif meter_length <= 150:
            color = (139, 0, 0)
        

        scroll -= 7

        for i in range(len(collectables)):
            collect_image = pygame.image.load(collectables[i].image_name)
            screen.blit(collect_image, (collectables[i].rect.x, collectables[i].rect.y))
            collectables[i].rect.x -= 7

        if abs(scroll) > bg_width:
            scroll = 0

        if not is_jumping:
            if count % 4 == 1:
                screen.blit(anime_run[0], player_rect)
            elif count % 4 == 2:
                screen.blit(anime_run[1], player_rect)
            elif count % 4 == 3:
                screen.blit(anime_run[2], player_rect)
            elif count % 4 == 0:
                screen.blit(anime_run[3], player_rect)

        else:
            player_rect.y += y_velocity
            y_velocity += gravity

            if jump_count <= 3:
                screen.blit(anime_jump[0], player_rect)
            elif jump_count <= 6:
                screen.blit(anime_jump[1], player_rect)
            elif jump_count <= 9:
                screen.blit(anime_jump[2], player_rect)
            elif jump_count >= 12:
                screen.blit(anime_jump[3], player_rect)
            
        jump_count += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if not is_jumping:
                        is_jumping = True
                        jump_count = 0
                        y_velocity = jump_velocity
                if event.key == K_ESCAPE:
                    m = 0
                    score = 0
                    meter_length = 20
                    initCollectables()
            # if event.type == MOUSEBUTTONDOWN:
            #     meter_length += 5

        for i in range(len(collectables)):
            if player_rect.colliderect(collectables[i]):
                if collectables[i].isgood == True:
                    collect_sound.play()
                else:
                    loss_sound.play()
                collectables[i].rect.y += 200
                score += collectables[i].score_boost
                if collectables[i].score_boost == 0:
                    score_boost_text = font.render("", True, (1, 50, 32))
                else:
                    if collectables[i].score_boost > 0:
                        score_boost_text = font.render("+" + str(collectables[i].score_boost), True, (1, 50, 32))
                    else:
                        score_boost_text = font.render(str(collectables[i].score_boost), True, (1, 50, 32))
                    boost_distance = 75
                score_boost_rect = score_boost_text.get_rect()
                score_boost_rect.bottomleft = (player_rect.topright)
                
                meter_length += collectables[i].footprint
                if (meter_length < 0):
                    meter_length = 0

        if boost_distance > 0:
            score_boost_rect.y -= 5
            boost_distance -= 5
            screen.blit(score_boost_text, score_boost_rect)

        if meter_length >= 150:
            m = 2
            loss_sound.play()
            meter_length = 20
            high_score = max(score, high_score)
            score = 0
            initCollectables()

        if player_rect.bottom > Height:
            is_jumping = False
            player_rect.bottom = Height
            jump_count = 0
            y_velocity = jump_velocity

        screen.blit(score_text, score_rect)
        screen.blit(high_score_text, high_score_rect)
        screen.blit(carbon_text, carbon_rect)
        
        pygame.display.update()