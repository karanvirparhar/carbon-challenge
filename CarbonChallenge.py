import pygame
import random
import math
from easygui import *
from pygame.locals import *
import json

pygame.init()

Width = 1500
Height = 500

clock = pygame.time.Clock()
FPS = 25

text = "Enter your Username"
title = "Login"
# d_text = "Enter here..."
name = enterbox(text, title)
lines = "\n" * 5
# spaces = " " * (len(name) * 5 - len(name) // 5)
text = "Welcome " + name + "!"
centered_text = text.center(80)

# msgbox(lines + centered_text, title="Welcome!")

with open("username.json", "r") as file:
    data = json.load(file)

score = 0
high_score = 0

if name in data:
    high_score = data[name]

if name == None:
    pygame.quit()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Carbon Challenge')

m = 3
sound = True

# def menu():
#     global m
#     global sound
#     # print("entered menu function")
#     screen.fill('black')
#     p = pygame.draw.rect(screen, 'orange', (Width//2 - 200, Height//2 - 50, 100, 50))
#     q = pygame.draw.rect(screen, 'orange', (Width//2 + 100, Height//2 - 50, 100, 50))
    
#     play_text = font.render("Play", True, 'white')
#     play_text_rect = play_text.get_rect()
#     play_text_rect.center = (p.center)

#     quit_text = font.render("Quit", True, 'white')
#     quit_text_rect = quit_text.get_rect()
#     quit_text_rect.center = (q.center)

#     s = pygame.draw.rect(screen, "orange", (0, Height//2 - 50, 120, 50))

#     sound_text = font.render("Sound", True, 'white')
#     sound_text_rect = sound_text.get_rect()
#     sound_text_rect.center = (s.center)

#     screen.blit(sound_text, sound_text_rect)
#     screen.blit(play_text, play_text_rect)
#     screen.blit(quit_text, quit_text_rect)

#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()

#         if event.type == MOUSEBUTTONDOWN:
#             if p.collidepoint(event.pos):
#                 m = 1
#                 # print("m after play clicked", m)
#             elif q.collidepoint(event.pos):
#                 pygame.quit()
#             elif s.collidepoint(event.pos):
#                 if sound == True or sound == "placeholder":
#                     sound = False
#                 elif sound == False:
#                     sound = True
#         if event.type == KEYDOWN:
#             if event.key == K_q:
#                 pygame.quit()
#                 exit()
    
    # if sound == True or sound == "placeholder":
    #     pygame.draw.rect(screen, 'red', (130, Height // 2 - 37.5, 25, 25))
    # elif sound == False:
    #     pygame.draw.rect(screen, 'red', (130, Height // 2 - 37.5, 25, 25), 5)

def game_over():
    global m
    global sound
    # print("entered menu function")
    screen.fill('black')
    p = pygame.draw.rect(screen, (149, 39, 39), (Width//2 - 200, Height//2 - 50, 100, 50))
    q = pygame.draw.rect(screen, (149, 39, 39), (Width//2 + 100, Height//2 - 50, 100, 50))
    s = pygame.draw.rect(screen, (149, 39, 39), (0, Height//2 - 50, 120, 50))

    game_over_text = font.render("Game Over!", True, 'red')
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (Width//2, Height//2 - 100)
    
    play_text = font.render("Play", True, 'pink')
    play_text_rect = play_text.get_rect()
    play_text_rect.center = (p.center)

    quit_text = font.render("Quit", True, 'pink')
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = (q.center)

    sound_text = font.render("Sound", True, 'pink')
    sound_text_rect = sound_text.get_rect()
    sound_text_rect.center = (s.center)

    screen.blit(play_text, play_text_rect)
    screen.blit(quit_text, quit_text_rect)
    screen.blit(game_over_text, game_over_text_rect)
    screen.blit(sound_text, sound_text_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if p.collidepoint(event.pos):
                m = 1
                # print("m after play clicked", m)
            elif q.collidepoint(event.pos):
                pygame.quit()
            elif s.collidepoint(event.pos):
                if sound == True or sound == "placeholder":
                    sound = False
                elif sound == False:
                    sound = True
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit()
        
    if sound == True or sound == "placeholder":
        pygame.draw.rect(screen, 'red', (130, Height // 2 - 37.5, 25, 25))
    elif sound == False:
        pygame.draw.rect(screen, 'red', (130, Height // 2 - 37.5, 25, 25), 5)

anime_run = []
anime_jump = []

bg = pygame.image.load("BG.jpg")

player_height = 0
is_jumping = False

font = pygame.font.Font("Font.otf", 40)

guide_font = pygame.font.Font("Font.otf", 32)
small_font = pygame.font.Font("Font.otf", 24)

carbon_text = font.render("Carbon Meter: ", True, (1, 50, 32))
carbon_rect = carbon_text.get_rect()
carbon_rect.topleft = (250, 10)

collect_sound = pygame.mixer.Sound("collect.wav")
loss_sound = pygame.mixer.Sound("loss.wav")

for i in range(1, 5):
    image_name = "player-run-" + str(i) + ".png"
    player_image = pygame.image.load(image_name)
    new_player_image = pygame.transform.scale(player_image, (72, 90))
    player_rect = new_player_image.get_rect()
    player_rect.centerx = Width//2
    player_rect.y = player_y = Height - new_player_image.get_height()
    anime_run.append(new_player_image)

for i in range(1, 3):
    image_name = "player-jump-" + str(i) + ".png"
    player_image = pygame.image.load(image_name)
    new_player_image = pygame.transform.scale(player_image, (72, 90))
    player_rect = new_player_image.get_rect()
    player_rect.centerx = Width//2
    player_rect.y = player_y = Height - new_player_image.get_height()
    anime_jump.append(new_player_image)

num_collectables = 100

class Collectable(pygame.sprite.Sprite):
    def __init__(self, image_name, score_boost, footprint, isgood, shield, issmog):
        super().__init__()
        self.image_name = image_name
        self.score_boost = score_boost
        self.footprint = footprint
        self.isgood = isgood
        self.shield = shield
        self.issmog = issmog
        self.rect = None

collectables = []

shield = Collectable("shield.png", 0, 0, True, True, False)

def initCollectables():
    global collectables
    collectables = []
    for i in range(num_collectables):
        chance = random.randint(1, 100)
        if chance <= 15:
            leaf = Collectable("leaf1.png", 2, -5, True, False, False)
            collectables.append(leaf)
        elif chance <= 30:
            panel = Collectable("panel1.png", 5, -10, True, False, False)
            collectables.append(panel)
        elif chance <= 45:
            evbattery = Collectable("evbattery.png", 10, -15, True, False, False)
            collectables.append(evbattery)
        elif chance <= 65:
            smog_cloud = Collectable("smog_cloud.png", 0, 30, False, False, True)
            collectables.append(smog_cloud)
        elif chance <= 80:
            oil_spill = Collectable("oil_spill.png", -5, 35, False, False, False)
            collectables.append(oil_spill)
        elif chance <= 90:
            water_bottle = Collectable("water_bottle.png", 2, 0, True, False, False)
            collectables.append(water_bottle)
        elif chance <= 99:
            factory = Collectable("factory.png", -10, 40, False, False, False)
            collectables.append(factory)
        elif chance <= 100:
            shield = Collectable("shield.png", 0, 0, True, True, False)
            collectables.append(shield)

    space = random.randint(25, 100)

    for i in range(len(collectables)):
        collect_image = pygame.image.load(collectables[i].image_name)
        collectables[i].rect = collect_image.get_rect()
        collectables[i].rect.x = Width + space
        ground = random.randint(0, 1)
        if collectables[i].issmog == True:
            collectables[i].rect.y = Height - collect_image.get_height() - 100 * ground
        else:
            collectables[i].rect.y = Height - collect_image.get_height()
        space += random.randint(200, 250)

initCollectables()

leaf_img = pygame.image.load("leaf1.png")
panel_img = pygame.image.load("panel1.png")
battery_img = pygame.image.load("evbattery.png")
bottle_img = pygame.image.load("water_bottle.png")
shield_img = pygame.image.load("shield.png")
smog_img = pygame.image.load("smog_cloud.png")
oil_img = pygame.image.load("oil_spill.png")
factory_img = pygame.image.load("factory.png")

def draw_guide():
    global m
    global sound

    screen.fill((240, 240, 240))  # Light gray background
    
    # Title moved up
    title = font.render("Let's Save Earth! - Game Collectibles Guide", True, (0, 0, 0))
    title_rect = title.get_rect(center=(750, 20))  # Moved up to y=15
    screen.blit(title, title_rect)
    
    # Headers - Wider for the larger screen
    pygame.draw.rect(screen, (76, 175, 80), (50, 40, 650, 50))  # Moved down slightly to y=40
    pygame.draw.rect(screen, (244, 67, 54), (800, 40, 650, 50))  # Moved down slightly to y=40
    
    good_header = font.render("Good Collectibles", True, (255, 255, 255))
    bad_header = font.render("Bad Collectibles", True, (255, 255, 255))
    
    # Centered headers in their rectangles
    good_header_rect = good_header.get_rect(center=(375, 65))  # Adjusted y to match new header position
    bad_header_rect = bad_header.get_rect(center=(1125, 65))  # Adjusted y to match new header position
    
    screen.blit(good_header, good_header_rect)
    screen.blit(bad_header, bad_header_rect)
    
    # Modified spacing for horizontal layout
    y_start = 100
    x_good_img = 80
    x_good_text = 180
    x_bad_img = 830
    x_bad_text = 930
    spacing = 75  # Vertical spacing between items
    
    # Good Collectibles - Left side
    # Leaf
    screen.blit(leaf_img, (x_good_img, y_start))
    text = guide_font.render("Leaf (+2 score, -5 carbon)", True, (0, 0, 0))
    desc = small_font.render("Helps save Earth", True, (100, 100, 100))
    screen.blit(text, (x_good_text, y_start))
    screen.blit(desc, (x_good_text, y_start + 35))
    
    # Solar Panel
    screen.blit(panel_img, (x_good_img, y_start + spacing))
    text = guide_font.render("Solar Panel (+5 score, -10 carbon)", True, (0, 0, 0))
    desc = small_font.render("Eco-friendly energy source", True, (100, 100, 100))
    screen.blit(text, (x_good_text, y_start + spacing))
    screen.blit(desc, (x_good_text, y_start + spacing + 35))
    
    # EV Battery
    screen.blit(battery_img, (x_good_img, y_start + spacing * 2))
    text = guide_font.render("EV Battery (+10 score, -15 carbon)", True, (0, 0, 0))
    desc = small_font.render("Reduces fossil fuel usage", True, (100, 100, 100))
    screen.blit(text, (x_good_text, y_start + spacing * 2))
    screen.blit(desc, (x_good_text, y_start + spacing * 2 + 35))
    
    # Water Bottle
    screen.blit(bottle_img, (x_good_img, y_start + spacing * 3))
    text = guide_font.render("Water Bottle (+2 score, 0 carbon)", True, (0, 0, 0))
    desc = small_font.render("Recyclable and reusable", True, (100, 100, 100))
    screen.blit(text, (x_good_text, y_start + spacing * 3))
    screen.blit(desc, (x_good_text, y_start + spacing * 3 + 35))
    
    # Shield
    screen.blit(shield_img, (x_good_img, y_start + spacing * 4))
    text = guide_font.render("Shield (30sec protection)", True, (0, 0, 0))
    desc = small_font.render("Temporary immunity", True, (100, 100, 100))
    screen.blit(text, (x_good_text, y_start + spacing * 4))
    screen.blit(desc, (x_good_text, y_start + spacing * 4 + 35))
    
    # Bad Collectibles - Right side
    # Smog Cloud
    screen.blit(smog_img, (x_bad_img, y_start))
    text = guide_font.render("Smog Cloud (0 score, +30 carbon)", True, (0, 0, 0))
    desc = small_font.render("Fossil fuel pollution", True, (100, 100, 100))
    screen.blit(text, (x_bad_text, y_start))
    screen.blit(desc, (x_bad_text, y_start + 35))
    
    # Oil Spill
    screen.blit(oil_img, (x_bad_img, y_start + spacing))
    text = guide_font.render("Oil Spill (-5 score, +35 carbon)", True, (0, 0, 0))
    desc = small_font.render("Environmental hazard", True, (100, 100, 100))
    screen.blit(text, (x_bad_text, y_start + spacing))
    screen.blit(desc, (x_bad_text, y_start + spacing + 35))
    
    # Factory
    screen.blit(factory_img, (x_bad_img, y_start + spacing * 2))
    text = guide_font.render("Factory (-10 score, +40 carbon)", True, (0, 0, 0))
    desc = small_font.render("High emissions source", True, (100, 100, 100))
    screen.blit(text, (x_bad_text, y_start + spacing * 2))
    screen.blit(desc, (x_bad_text, y_start + spacing * 2 + 35))
    
    # Add instructions at bottom
    exit_text = small_font.render("Press ESC to exit", True, (100, 100, 100))
    exit_rect = exit_text.get_rect(center=(750, 470))
    screen.blit(exit_text, exit_rect)

    p = pygame.draw.rect(screen, (149, 39, 39), (700, 400, 100, 50))
    # q = pygame.draw.rect(screen, 'orange', (1050, 420, 100, 50))
    
    play_text = font.render("Play", True, 'pink')
    play_text_rect = play_text.get_rect()
    play_text_rect.center = (p.center)

    # quit_text = font.render("Quit", True, 'white')
    # quit_text_rect = quit_text.get_rect()
    # quit_text_rect.center = (q.center)

    s = pygame.draw.rect(screen, (149, 39, 39), (Width - 175, 400, 120, 50))

    sound_text = font.render("Sound", True, 'pink')
    sound_text_rect = sound_text.get_rect()
    sound_text_rect.center = (s.center)

    screen.blit(sound_text, sound_text_rect)
    screen.blit(play_text, play_text_rect)
    # screen.blit(quit_text, quit_text_rect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == MOUSEBUTTONDOWN:
            # if event.button == 1:
            if p.collidepoint(event.pos):
                m = 1
            elif s.collidepoint(event.pos):
                if sound == True or sound == "placeholder":
                    sound = False
                    # print("Sound is set to false")
                elif sound == False:
                    sound = True
                    # print("Sound is set to true")
        
    # print("Exiting draw_guide...")
    if sound == True or sound == "placeholder":
        pygame.draw.rect(screen, 'red', (1460, 412.5, 25, 25))
    elif sound == False:
        pygame.draw.rect(screen, 'red', (1460, 412.5, 25, 25), 5)

encounters = {}
instructions = {"leaf1.png": "Catch this! Leaves and trees are important for saving Earth.",
                "panel1.png": "Solar panels are eco-friendly renewable energy sources. Collect them for a greener world.",
                "evbattery.png": "Electrical car batteries reduce usage of fossil fuels. Pick them up when you see them.",
                "smog_cloud.png": "Smog clouds are a type of pollution caused by the burning of fossil fuels. Avoid them!",
                "oil_spill.png": "Oil spills are dangerous for our environment. Jump over them to win.",
                "water_bottle.png": "Recyclable water bottles help in making a greener Earth. They are reusable and lessen fossil fuel emmisions.",
                "factory.png": "Factory emissions are horrible for Earth's climate. Avoid them to win the game."}

bg_width = bg.get_width()
tiles = math.ceil(Width / bg_width) + 1

def show_instruction_popup(collecteditem):
    global sound
    global bg_width
    global tiles
    if not collecteditem.image_name in encounters:
        encounters[collecteditem.image_name] = 1
        popup_font = pygame.font.SysFont("Comic Sans", 25)
        if collecteditem.image_name in instructions:
            popup_text = popup_font.render(instructions[collecteditem.image_name], True, (1, 50, 32))
        popup_text_rect = popup_text.get_rect()
        popup_text_rect.center = (Width//2, Height//2)

        # pygame.draw.rect(screen, 'orange', (popup_text_rect.centerx - popup_text_rect.width//2 - 10, popup_text_rect.y - 10, popup_text_rect.width + 20, popup_text_rect.height + 20))

        pygame.display.update()

        running = True
        while running:
            score_text = font.render("Score: " + str(score), True, (0, 0, 139))
            score_rect = score_text.get_rect()
            score_rect.topleft = (10, 10)
            high_score_text = font.render("High Score: " + str(high_score), True, (0, 0, 139))
            high_score_rect = high_score_text.get_rect()
            high_score_rect.topleft = (1100, 10)

            for i in range(0, tiles):
                screen.blit(bg, (i * bg_width + scroll - (i * line), 0))

            screen.blit(score_text, score_rect)
            screen.blit(high_score_text, high_score_rect)
            if timer >= 0:
                screen.blit(timer_text, timer_text_rect)
            screen.blit(carbon_text, carbon_rect)

            carbon = pygame.draw.rect(screen, color, (520, 23, meter_length, 15))
            pygame.draw.rect(screen, (139, 0, 0), (520, 23, limit, 15), 1)

            s = pygame.draw.rect(screen, (149, 39, 39), (0, Height//2 - 50, 120, 50))

            sound_text = font.render("Sound", True, 'white')
            sound_text_rect = sound_text.get_rect()
            sound_text_rect.center = (s.center)

            screen.blit(sound_text, sound_text_rect)

            for i in range(len(collectables)):
                collect_image = pygame.image.load(collectables[i].image_name)
                screen.blit(collect_image, (collectables[i].rect.x, collectables[i].rect.y))

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
                if jump_count <= 3:
                    screen.blit(anime_jump[0], player_rect)
                elif jump_count >= 4:
                    screen.blit(anime_jump[1], player_rect)

            pygame.draw.rect(screen, 'orange', (popup_text_rect.x, popup_text_rect.y, popup_text_rect.width + 10, popup_text_rect.height + 10))
            pygame.draw.rect(screen, 'white', popup_text_rect)
            screen.blit(popup_text, popup_text_rect)

            if activate_shield:
                shield_image = pygame.image.load(shield.image_name)
                shield_rect = shield_image.get_rect()
                shield_rect.center = player_rect.center
                screen.blit(shield_image, shield_rect)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_SPACE:
                        running = False
                    if event.key == K_q:
                        pygame.quit()
                        exit()
                if event.type == MOUSEBUTTONDOWN:
                    if s.collidepoint(event.pos) and event.button == 1:
                        if sound == True or sound == "placeholder":
                            sound = False
                        elif sound == False:
                            sound = True
                    if event.button == 1:
                        running = False
            
            if sound == True or sound == "placeholder":
                pygame.draw.rect(screen, 'red', (130, Height // 2 - 37.5, 25, 25))
            else:
                pygame.draw.rect(screen, 'red', (130, Height // 2 - 37.5, 25, 25), 5)

            pygame.display.update()

            if sound == False:
                pygame.mixer.music.pause()
            elif sound == True:
                pygame.mixer.music.unpause()
                sound = "placeholder"

scroll = 0
collectable_scroll = 7
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

# transparent_surface = pygame.Surface((player_rect.x, player_rect.y), pygame.SRCALPHA)
# color = (0, 0, 139, 128)

boost_distance = 75
activate_shield = False

color = 'green'
limit = 100

timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 1000)
timer = -1

# def get_high_score():
#     with open("score.txt", "r") as file:
#         return int(file.read())

# def save_high_score(score):
#     with open("score.txt", "w") as file:
#         file.write(str(score))

while True:
    clock.tick(FPS)

    if sound == False:
        # print("Sound is false in while")
        pygame.mixer.music.pause()
    elif sound == True:
        # print("Sound is true in while")
        pygame.mixer.music.unpause()
        sound = "placeholder"

    # if m == 0:
    #     menu()
    #     pygame.display.update()

    if m == 3:
        draw_guide()
        pygame.display.update()

    elif m == 2:
        game_over()
        pygame.display.update()

    elif m == 1:
        count += 1

        if collectables[num_collectables - 1].rect.x < - collectables[num_collectables - 1].rect.width:
            initCollectables()

        #Update Score
        score_text = font.render("Score: " + str(score), True, (0, 0, 139))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)
        high_score_text = font.render("High Score: " + str(high_score), True, (0, 0, 139))
        high_score_rect = high_score_text.get_rect()
        high_score_rect.topleft = (1100, 10)
        
        if len(str(timer % 60)) > 1:
            timer_text = font.render("Shield Timer: " + str(timer // 60) + ": " + str(timer % 60), True, 'purple')
        else:
            timer_text = font.render("Shield Timer: " + str(timer // 60) + ": " + "0" + str(timer % 60), True, 'purple')
        timer_text_rect = timer_text.get_rect()
        timer_text_rect = (700, 10)

        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))

        screen.blit(score_text, score_rect)
        screen.blit(high_score_text, high_score_rect)
        if timer >= 0:
            screen.blit(timer_text, timer_text_rect)
        screen.blit(carbon_text, carbon_rect)

        carbon = pygame.draw.rect(screen, color, (520, 23, meter_length, 15))
        pygame.draw.rect(screen, (139, 0, 0), (520, 23, limit, 15), 1)
        
        s = pygame.draw.rect(screen, (149, 39, 39), (0, Height//2 - 50, 120, 50))

        sound_text = font.render("Sound", True, 'white')
        sound_text_rect = sound_text.get_rect()
        sound_text_rect.center = (s.center)

        screen.blit(sound_text, sound_text_rect)

        if meter_length <= 33:
            color = 'green'
        elif meter_length <= 66:
            color = 'orange'
        elif meter_length <= limit:
            color = (139, 0, 0)

        if score <= 75:
            scroll -= 7
        elif score <= 150:
            scroll -= 8
        elif score <= 225:
            scroll -= 9
        elif score > 225:
            scroll -= 10
        # elif score <= 375:
        #     scroll -= 11
        # elif score > 375:
        #     scroll -= 12

        for i in range(len(collectables)):
            collect_image = pygame.image.load(collectables[i].image_name)
            screen.blit(collect_image, (collectables[i].rect.x, collectables[i].rect.y))
            collectables[i].rect.x -= collectable_scroll
        
        if score <= 75:
            collectable_scroll = 7
        elif score <= 150:
            collectable_scroll = 8
        elif score <= 225:
            collectable_scroll = 9
        elif score > 225:
            collectable_scroll = 10
        # elif score <= 375:
        #     collectable_scroll = 11
        # elif score > 375:
        #     collectable_scroll = 12

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
            elif jump_count >= 4:
                screen.blit(anime_jump[1], player_rect)

        if activate_shield:
            shield_image = pygame.image.load(shield.image_name)
            shield_rect = shield_image.get_rect()
            shield_rect.center = player_rect.center
            screen.blit(shield_image, shield_rect)
            
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
                    m = 3
                    score = 0
                    timer = -1
                    player_rect.centerx = Width//2
                    player_rect.y = player_y
                    is_jumping = False
                    activate_shield = False
                    meter_length = 20
                    boost_distance = 0
                    initCollectables()
                    high_score = max(score, high_score)
                    data[name] = high_score
                    with open("username.json", "w") as file:
                        json.dump(data, file, indent=4)
                if event.key == K_q:
                    pygame.quit()
                    exit()
            if event.type == timer_event:
                if timer >= 0:
                    timer -= 1
            if event.type == MOUSEBUTTONDOWN:
                if s.collidepoint(event.pos):
                    if sound == True or sound == "placeholder":
                        sound = False
                    elif sound == False:
                        sound = True
                # if event.button == 1:
                #     if not is_jumping:
                #         is_jumping = True
                #         jump_count = 0
                #         y_velocity = jump_velocity

        if sound == True or sound == "placeholder":
            pygame.draw.rect(screen, 'red', (130, Height // 2 - 37.5, 25, 25))
        elif sound == False:
            pygame.draw.rect(screen, 'red', (130, Height // 2 - 37.5, 25, 25), 5)

        if timer < 0:
            activate_shield = False

        for i in range(len(collectables)):
            if player_rect.colliderect(collectables[i]):
                if sound != False:
                    if collectables[i].isgood == True:
                        collect_sound.play()
                    else:
                        loss_sound.play()
                if collectables[i].isgood == False:
                    if activate_shield:
                        collectables[i].score_boost = 0
                        collectables[i].footprint = 0
                if collectables[i].shield == True:
                    activate_shield = True
                    if timer == -1:
                        timer = 0
                    timer += 30
                else:
                    show_instruction_popup(collectables[i])
                collectables[i].rect.y += 200
                score += collectables[i].score_boost
                high_score = max(score, high_score)
                # save_high_score(high_score)
                data[name] = high_score
                with open("username.json", "w") as file:
                    json.dump(data, file, indent=4)
                if collectables[i].score_boost == 0:
                    score_boost_text = font.render("", True, (1, 50, 32))
                else:
                    if collectables[i].score_boost > 0:
                        score_boost_text = font.render("+" + str(collectables[i].score_boost), True, (1, 50, 32))
                    elif collectables[i].score_boost < 0:
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

        if meter_length >= limit:
            m = 2
            if sound != False:
                loss_sound.play()
            meter_length = 20
            boost_distance = 0
            score = 0
            initCollectables()
            activate_shield = False
            timer = -1
            player_rect.centerx = Width//2
            player_rect.y = player_y
            is_jumping = False

        if player_rect.bottom > Height:
            is_jumping = False
            player_rect.bottom = Height
            jump_count = 0
            y_velocity = jump_velocity
        
        pygame.display.update()