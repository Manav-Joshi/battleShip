import pygame, sys
import random
import math
import os
import time
menu = False
game = False
running = True
helpm = False
option = False
intro = True
end = False
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
font_folder = os.path.join(game_folder, 'font')
snd_folder = os.path.join(game_folder, 'snd')
result = 'draw'
volume = 0.5
WIDTH = 1200
HEIGHT = 780
FPS = 60
colChange = 0
#define colors
WHITE = (255, 255, 255)
GREY = (180,180,180)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255,0)
TEXTCOL = 0
TEXTCOL1 = 0
TEXTCOL2 = 0
guesser = 'a'
phase = 1
rotate = 1
aiguess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
#############################GRIDS#############################
p1 = [0,0,0,0,0,0,0,0]
p2 = [0,0,0,0,0,0,0,0]
p3 = [0,0,0,0,0,0,0,0]
p4 = [0,0,0,0,0,0,0,0]
p5 = [0,0,0,0,0,0,0,0]
p6 = [0,0,0,0,0,0,0,0]
p7 = [0,0,0,0,0,0,0,0]
p8 = [0,0,0,0,0,0,0,0]
#AI#
a1 = [0,0,0,0,0,0,0,0]
a2 = [0,0,0,0,0,0,0,0]
a3 = [0,0,0,0,0,0,0,0]
a4 = [0,0,0,0,0,0,0,0]
a5 = [0,0,0,0,0,0,0,0]
a6 = [0,0,0,0,0,0,0,0]
a7 = [0,0,0,0,0,0,0,0]
a8 = [0,0,0,0,0,0,0,0]
#############################GRIDS#############################
#initialize pygame and create window
pygame.init()
pygame.mixer.pre_init(44100,16,2,4096)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BATTLESHIP")
clock = pygame.time.Clock()
font = pygame.font.Font(os.path.join(font_folder,'font.ttf'), 40)
font2 = pygame.font.Font(os.path.join(font_folder,'font.ttf'), 12)
font1 = pygame.font.Font(os.path.join(font_folder,'font.ttf'), 70)
bg = pygame.image.load(os.path.join(img_folder,'bg.jpg'))
bg = pygame.transform.scale(bg,(1200,800))
bg_rect = bg.get_rect()
bg_rect.center = (WIDTH/2,HEIGHT/2 - 20)
def generator():
    rowai = random.randint(1,6)
    rowai1 = random.randint(1,6)
    colai = random.randint(0,7)
    colai1 = random.randint(0,7)
    rowai2 = random.randint(1,8)
    colai2 = random.randint(0,5)
    if rowai2 == 1:
        a1[colai2] = 1
        a1[colai2 + 1] = 1
        a1[colai2 + 2] = 1
    if rowai2 == 2:
        a2[colai2] = 1
        a2[colai2 + 1] = 1
        a2[colai2 + 2] = 1
    if rowai2 == 3:
        a3[colai2] = 1
        a3[colai2 + 1] = 1
        a3[colai2 + 2] = 1
    if rowai2 == 4:
        a4[colai2] = 1
        a4[colai2 + 1] = 1
        a4[colai2 + 2] = 1
    if rowai2 == 5:
        a5[colai2] = 1
        a5[colai2 + 1] = 1
        a5[colai2 + 2] = 1
    if rowai2 == 6:
        a6[colai2] = 1
        a6[colai2 + 1] = 1
        a6[colai2 + 2] = 1
    if rowai2 == 7:
        a7[colai2] = 1
        a7[colai2 + 1] = 1
        a7[colai2 + 2] = 1
    if rowai2 == 8:
        a8[colai2] = 1
        a8[colai2 + 1] = 1
        a8[colai2 + 2] = 1

    if rowai == 1:
        a1[colai] = 1
        a2[colai] = 1
        a3[colai] = 1
    if rowai == 2:
        a2[colai] = 1
        a4[colai] = 1
        a3[colai] = 1
    if rowai == 3:
        a3[colai] = 1
        a4[colai] = 1
        a5[colai] = 1
    if rowai == 4:
        a4[colai] = 1
        a5[colai] = 1
        a6[colai] = 1
    if rowai == 5:
        a5[colai] = 1
        a6[colai] = 1
        a7[colai] = 1
    if rowai == 6:
        a6[colai] = 1
        a7[colai] = 1
        a8[colai] = 1
    if rowai1 == 1:
        a1[colai1] = 1
        a2[colai1] = 1
        a3[colai1] = 1
    if rowai1 == 2:
        a2[colai1] = 1
        a4[colai1] = 1
        a3[colai1] = 1
    if rowai1 == 3:
        a3[colai1] = 1
        a4[colai1] = 1
        a5[colai1] = 1
    if rowai1 == 4:
        a4[colai1] = 1
        a5[colai1] = 1
        a6[colai1] = 1
    if rowai1 == 5:
        a5[colai1] = 1
        a6[colai1] = 1
        a7[colai1] = 1
    if rowai1 == 6:
        a6[colai1] = 1
        a7[colai1] = 1
        a8[colai1] = 1
    
 
def guess(guessn,guesser):
    raw = guessn/8
    row = math.ceil(raw)
    col = guessn % 8
    if row == 1:
        if guesser == 'p':
            if a1[col - 1] == 0:
                a1[col - 1] = 2
            elif a1[col - 1] == 1:
                a1[col - 1] = 3
        if guesser == 'a':
            if p1[col - 1] == 0:
                p1[col - 1] = 2
            elif p1[col - 1] == 1:
                p1[col - 1] = 3
    if row == 2:
        if guesser == 'p':
            if a2[col - 1] == 0:
                a2[col - 1] = 2
            elif a2[col - 1] == 1:
                a2[col - 1] = 3
        if guesser == 'a':
            if p2[col - 1] == 0:
                p2[col - 1] = 2
            elif p2[col - 1] == 1:
                p2[col - 1] = 3
    if row == 3:
        if guesser == 'p':
            if a3[col - 1] == 0:
                a3[col - 1] = 2
            elif a3[col - 1] == 1:
                a3[col - 1] = 3
        if guesser == 'a':
            if p3[col - 1] == 0:
                p3[col - 1] = 2
            elif p3[col - 1] == 1:
                p3[col - 1] = 3
    if row == 4:
        if guesser == 'p':
            if a4[col - 1] == 0:
                a4[col - 1] = 2
            elif a4[col - 1] == 1:
                a4[col - 1] = 3
        if guesser == 'a':
            if p4[col - 1] == 0:
                p4[col - 1] = 2
            elif p4[col - 1] == 1:
                p4[col - 1] = 3
    if row == 5:
        if guesser == 'p':
            if a5[col - 1] == 0:
                a5[col - 1] = 2
            elif a5[col - 1] == 1:
                a5[col - 1] = 3
        if guesser == 'a':
            if p5[col - 1] == 0:
                p5[col - 1] = 2
            elif p5[col - 1] == 1:
                p5[col - 1] = 3
    if row == 6:
        if guesser == 'p':
            if a6[col - 1] == 0:
                a6[col - 1] = 2
            elif a6[col - 1] == 1:
                a6[col - 1] = 3
        if guesser == 'a':
            if p6[col - 1] == 0:
                p6[col - 1] = 2
            elif p6[col - 1] == 1:
                p6[col - 1] = 3
    if row == 7:
        if guesser == 'p':
            if a7[col - 1] == 0:
                a7[col - 1] = 2
            elif a7[col - 1] == 1:
                a7[col - 1] = 3
        if guesser == 'a':
            if p7[col - 1] == 0:
                p7[col - 1] = 2
            elif p7[col - 1] == 1:
                p7[col - 1] = 3
    if row == 8:
        if guesser == 'p':
            if a8[col - 1] == 0:
                a8[col - 1] = 2
            elif a8[col - 1] == 1:
                a8[col - 1] = 3
        if guesser == 'a':
            if p8[col - 1] == 0:
                p8[col - 1] = 2
            elif p8[col - 1] == 1:
                p8[col - 1] = 3

bgm = pygame.mixer.music.load("bgm.mp3")
fire = pygame.mixer.Sound('cannon.wav')
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)

gameStart = font.render('Play', True, WHITE) 
gameButton = gameStart.get_rect()
gameButton.center = (WIDTH/2 - 100,HEIGHT - 30)

helpB = font.render('Help', True, WHITE) 
helpButton = helpB.get_rect()
helpButton.center = (WIDTH/2 + 100,HEIGHT - 30)

text = font.render('Enemy Grid ---', True, WHITE) 
textt = text.get_rect()
textt.midleft = (10,20)

text1 = font.render('Your Grid ', True, WHITE) 
textt1 = text1.get_rect()
textt1.midleft = (10,60)

generator()

#Game Loop
while running:
    clock.tick(FPS)
    while intro:
        clock.tick(FPS)
        SCREEN.fill(BLACK)
        colChange += 1
        if colChange > 4 and colChange < 259:
            TEXTCOL += 1
        if colChange > 280 and colChange < (255 + 280):
            TEXTCOL -= 1
            TEXTCOL1 += 1
        if colChange > (255 + 280 + 20) and colChange < (255 + 255 + 280 + 20):
            TEXTCOL1 -= 1
            TEXTCOL2 += 1
        if colChange == (255 + 255 + 280 + 20 + 40 + 90):
            intro = False
            menu = True
        iden = font.render('A Game by Manav', True, (TEXTCOL,TEXTCOL,TEXTCOL))
        iden1 = font.render('Presenting', True, (TEXTCOL1,TEXTCOL1,TEXTCOL1))
        iden2 = font1.render('BATTLESHIP', True, (TEXTCOL2,TEXTCOL2,TEXTCOL2))
        idenr = iden.get_rect()
        idenr.center = (WIDTH/2,HEIGHT/2 - 50)
        idenr1 = iden1.get_rect()
        idenr1.center = (WIDTH/2,HEIGHT/2)
        idenr2 = iden2.get_rect()
        idenr2.center = (WIDTH/2,HEIGHT/2 + 100)
        SCREEN.blit(iden,idenr)
        SCREEN.blit(iden1,idenr1)
        SCREEN.blit(iden2,idenr2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                running = False
        pygame.display.flip()
    while end:
        SCREEN.fill(BLACK)
        if result == 'win':
            rtext = font.render('Outstanding victory, Admiral.', True, WHITE) 
            rtext1 = rtext.get_rect()
            rtext1.center = (WIDTH/2,HEIGHT/2)
        elif result == 'loss':
            rtext = font.render('Understandable Defeat, Admiral..', True, WHITE) 
            rtext1 = rtext.get_rect()
            rtext1.center = (WIDTH/2,HEIGHT/2)
        SCREEN.blit(rtext,rtext1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                end = False
                menu = True
        pygame.display.flip()
    while menu:
        clock.tick(FPS)
        SCREEN.fill(BLACK)
        SCREEN.blit(bg,bg_rect)
        SCREEN.blit(gameStart, gameButton)
        SCREEN.blit(helpB, helpButton)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gameButton.collidepoint(pygame.mouse.get_pos()):
                    menu = False
                    game = True
                if helpButton.collidepoint(pygame.mouse.get_pos()):
                    menu = False
                    helpm = True
        pygame.display.flip()
    while game:
        if phase == 999999:
            text2 = font.render('Player wins', True, WHITE)
            result = 'win'
            pygame.display.flip()
            phase = -1
        if phase == -1:
            p1 = [0,0,0,0,0,0,0,0]
            p2 = [0,0,0,0,0,0,0,0]
            p3 = [0,0,0,0,0,0,0,0]
            p4 = [0,0,0,0,0,0,0,0]
            p5 = [0,0,0,0,0,0,0,0]
            p6 = [0,0,0,0,0,0,0,0]
            p7 = [0,0,0,0,0,0,0,0]
            p8 = [0,0,0,0,0,0,0,0]
            #AI#
            a1 = [0,0,0,0,0,0,0,0]
            a2 = [0,0,0,0,0,0,0,0]
            a3 = [0,0,0,0,0,0,0,0]
            a4 = [0,0,0,0,0,0,0,0]
            a5 = [0,0,0,0,0,0,0,0]
            a6 = [0,0,0,0,0,0,0,0]
            a7 = [0,0,0,0,0,0,0,0]
            a8 = [0,0,0,0,0,0,0,0]
            phase = 1
            aiguess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
            game = False
            menu = False
            end = True
        if phase == 111111:
            text2 = font.render('Computer wins', True, WHITE)
            result = 'loss'
            pygame.display.flip()
            phase = -1
        if phase <= 3:
            text2 = font.render('Deploy Phase', True, WHITE)
        if phase > 3 and phase != 999999:
            text2 = font.render('Firing Phase', True, WHITE)
        textt2 = text2.get_rect()
        textt2.midleft = (10,HEIGHT - 30)
        clock.tick(FPS)
        SCREEN.fill(BLACK)
        SCREEN.blit(text,textt)
        SCREEN.blit(text1,textt1)
        SCREEN.blit(text2,textt2)
        if phase <= 3:
            for i in range (0,8):
                if p1[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [400 + (i * 100), 0,100,100])
            for i in range (0,8):
                if p2[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [400 + (i * 100), 100,100,100])
            for i in range (0,8):
                if p3[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [400 + (i * 100), 200,100,100])
            for i in range (0,8):
                if p4[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [400 + (i * 100), 300,100,100])
            for i in range (0,8):
                if p5[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [400 + (i * 100), 400,100,100])
            for i in range (0,8):
                if p6[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [400 + (i * 100), 500,100,100])
            for i in range (0,8):
                if p7[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [400 + (i * 100), 600,100,100])
            for i in range (0,8):
                if p8[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [400 + (i * 100), 700,100,100])
        if phase > 3:
            for i in range (0,8):
                if p1[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [10 + (i * 30), 100,30,30])
            for i in range (0,8):
                if p2[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [10 + (i * 30), 130,30,30])
            for i in range (0,8):
                if p3[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [10 + (i * 30), 160,30,30])
            for i in range (0,8):
                if p4[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [10 + (i * 30), 190,30,30])
            for i in range (0,8):
                if p5[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [10 + (i * 30), 220,30,30])
            for i in range (0,8):
                if p6[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [10 + (i * 30), 250,30,30])
            for i in range (0,8):
                if p7[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [10 + (i * 30), 280,30,30])
            for i in range (0,8):
                if p8[i] == 1:
                    pygame.draw.rect(SCREEN, WHITE, [10 + (i * 30), 310,30,30])
                    ## YOUR FIRING
            for i in range (0,8):
                if a1[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [400 + (i * 100), 0,100,100])
            for i in range (0,8):
                if a2[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [400 + (i * 100), 100,100,100])
            for i in range (0,8):
                if a3[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [400 + (i * 100), 200,100,100])
            for i in range (0,8):
                if a4[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [400 + (i * 100), 300,100,100])
            for i in range (0,8):
                if a5[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [400 + (i * 100), 400,100,100])
            for i in range (0,8):
                if a6[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [400 + (i * 100), 500,100,100])
            for i in range (0,8):
                if a7[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [400 + (i * 100), 600,100,100])
            for i in range (0,8):
                if a8[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [400 + (i * 100), 700,100,100])
                    ## AI FIRING
            for i in range (0,8):
                if p1[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [10 + (i * 30), 100,30,30])
            for i in range (0,8):
                if p2[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [10 + (i * 30), 130,30,30])
            for i in range (0,8):
                if p3[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [10 + (i * 30), 160,30,30])
            for i in range (0,8):
                if p4[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [10 + (i * 30), 190,30,30])
            for i in range (0,8):
                if p5[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [10 + (i * 30), 220,30,30])
            for i in range (0,8):
                if p6[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [10 + (i * 30), 250,30,30])
            for i in range (0,8):
                if p7[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [10 + (i * 30), 280,30,30])
            for i in range (0,8):
                if p8[i] == 2:
                    pygame.draw.rect(SCREEN, GREY, [10 + (i * 30), 310,30,30])
            ## IF AI HITS YOU
            for i in range (0,8):
                if p1[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [10 + (i * 30), 100,30,30])
            for i in range (0,8):
                if p2[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [10 + (i * 30), 130,30,30])
            for i in range (0,8):
                if p3[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [10 + (i * 30), 160,30,30])
            for i in range (0,8):
                if p4[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [10 + (i * 30), 190,30,30])
            for i in range (0,8):
                if p5[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [10 + (i * 30), 220,30,30])
            for i in range (0,8):
                if p6[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [10 + (i * 30), 250,30,30])
            for i in range (0,8):
                if p7[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [10 + (i * 30), 280,30,30])
            for i in range (0,8):
                if p8[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [10 + (i * 30), 310,30,30])
            ## IF YOU HIT AI
            for i in range (0,8):
                if a1[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [400 + (i * 100), 0,100,100])
            for i in range (0,8):
                if a2[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [400 + (i * 100), 100,100,100])
            for i in range (0,8):
                if a3[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [400 + (i * 100), 200,100,100])
            for i in range (0,8):
                if a4[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [400 + (i * 100), 300,100,100])
            for i in range (0,8):
                if a5[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [400 + (i * 100), 400,100,100])
            for i in range (0,8):
                if a6[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [400 + (i * 100), 500,100,100])
            for i in range (0,8):
                if a7[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [400 + (i * 100), 600,100,100])
            for i in range (0,8):
                if a8[i] == 3:
                    pygame.draw.rect(SCREEN, RED, [400 + (i * 100), 700,100,100])

        pygame.draw.line(SCREEN, WHITE,[10,100],[10,340],1)
        pygame.draw.line(SCREEN, WHITE,[40,100],[40,340],1)
        pygame.draw.line(SCREEN, WHITE,[70,100],[70,340],1)
        pygame.draw.line(SCREEN, WHITE,[100,100],[100,340],1)
        pygame.draw.line(SCREEN, WHITE,[130,100],[130,340],1)
        pygame.draw.line(SCREEN, WHITE,[160,100],[160,340],1)
        pygame.draw.line(SCREEN, WHITE,[190,100],[190,340],1)
        pygame.draw.line(SCREEN, WHITE,[220,100],[220,340],1)
        pygame.draw.line(SCREEN, WHITE,[250,100],[250,340],1)

        pygame.draw.line(SCREEN, WHITE,[10,100],[250,100],1)
        pygame.draw.line(SCREEN, WHITE,[10,130],[250,130],1)
        pygame.draw.line(SCREEN, WHITE,[10,160],[250,160],1)
        pygame.draw.line(SCREEN, WHITE,[10,190],[250,190],1)
        pygame.draw.line(SCREEN, WHITE,[10,220],[250,220],1)
        pygame.draw.line(SCREEN, WHITE,[10,250],[250,250],1)
        pygame.draw.line(SCREEN, WHITE,[10,280],[250,280],1)
        pygame.draw.line(SCREEN, WHITE,[10,310],[250,310],1)
        pygame.draw.line(SCREEN, WHITE,[10,340],[250,340],1)
        
        
        #draw the lines for the big grid
        pygame.draw.line(SCREEN, WHITE,[400,0],[1200,0],1)
        pygame.draw.line(SCREEN, WHITE,[400,100],[1200,100],1)
        pygame.draw.line(SCREEN, WHITE,[400,200],[1200,200],1)
        pygame.draw.line(SCREEN, WHITE,[400,300],[1200,300],1)
        pygame.draw.line(SCREEN, WHITE,[400,400],[1200,400],1)
        pygame.draw.line(SCREEN, WHITE,[400,500],[1200,500],1)
        pygame.draw.line(SCREEN, WHITE,[400,600],[1200,600],1)
        pygame.draw.line(SCREEN, WHITE,[400,700],[1200,700],1)
        pygame.draw.line(SCREEN, WHITE,[400,800],[1200,800],1)
        
        pygame.draw.line(SCREEN, WHITE,[400,0],[400,800],1)
        pygame.draw.line(SCREEN, WHITE,[500,0],[500,800],1)
        pygame.draw.line(SCREEN, WHITE,[600,0],[600,800],1)
        pygame.draw.line(SCREEN, WHITE,[700,0],[700,800],1)
        pygame.draw.line(SCREEN, WHITE,[800,0],[800,800],1)
        pygame.draw.line(SCREEN, WHITE,[900,0],[900,800],1)
        pygame.draw.line(SCREEN, WHITE,[1000,0],[1000,800],1)
        pygame.draw.line(SCREEN, WHITE,[1100,0],[1100,800],1)
        pygame.draw.line(SCREEN, WHITE,[1199,0],[1199,800],5)
        for event in pygame.event.get():
            if event.type == pygame. KEYDOWN:
                if event.unicode == 'r' or event.unicode == 'R':
                    if rotate == 1:
                        rotate = 2
                    elif rotate == 2:
                        rotate = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if phase <= 3:
                    phase += 1
                    colD = math.ceil((mx - 400)/100) - 1
                    rowD = math.ceil(my/100)
                    if rotate == 1:
                        if rowD == 1:
                            p1[colD] = 1
                            p2[colD] = 1
                            p3[colD] = 1
                        if rowD == 2:
                            p2[colD] = 1
                            p3[colD] = 1
                            p4[colD] = 1
                        if rowD == 3:
                            p3[colD] = 1
                            p4[colD] = 1
                            p5[colD] = 1
                        if rowD == 4:
                            p4[colD] = 1
                            p5[colD] = 1
                            p6[colD] = 1
                        if rowD == 5:
                            p5[colD] = 1
                            p6[colD] = 1
                            p7[colD] = 1
                        if rowD == 6:
                            p6[colD] = 1
                            p7[colD] = 1
                            p8[colD] = 1
                    if rotate == 2 and colD <= 5:
                        if rowD == 1:
                            p1[colD] = 1
                            p1[colD + 1] = 1
                            p1[colD + 2] = 1
                        if rowD == 2:
                            p2[colD] = 1
                            p2[colD + 1] = 1
                            p2[colD + 2] = 1
                        if rowD == 3:
                            p3[colD] = 1
                            p3[colD + 1] = 1
                            p3[colD + 2] = 1
                        if rowD == 4:
                            p4[colD] = 1
                            p4[colD + 1] = 1
                            p4[colD + 2] = 1
                        if rowD == 5:
                            p5[colD] = 1
                            p5[colD + 1] = 1
                            p5[colD + 2] = 1
                        if rowD == 6:
                            p6[colD] = 1
                            p6[colD + 1] = 1
                            p6[colD + 2] = 1
                        if rowD == 7:
                            p7[colD] = 1
                            p7[colD + 1] = 1
                            p7[colD + 2] = 1
                        if rowD == 8:
                            p8[colD] = 1
                            p8[colD + 1] = 1
                            p8[colD + 2] = 1
                if phase > 3:
                    colD = math.ceil((mx - 400)/100)
                    rowD = math.ceil(my/100)
                    guess(((rowD * 8) - 8) + colD,'p')
                    tguess = random.choice(aiguess)
                    fire.play()
                    aiguess.remove(tguess)
                    guess(tguess,'a')
                if 1 not in a1:
                    if 1 not in a2:
                        if 1 not in a3:
                            if 1 not in a4:
                                if 1 not in a5:
                                    if 1 not in a6:
                                        if 1 not in a7:
                                            if 1 not in a8:
                                                 phase = 999999
                if 1 not in p1:
                    if 1 not in p2:
                        if 1 not in p3:
                            if 1 not in p4:
                                if 1 not in p5:
                                    if 1 not in p6:
                                        if 1 not in p7:
                                            if 1 not in p8:
                                                 phase = 111111
                                                
            if event.type == pygame.QUIT:
                running = False
                exit()
        pygame.display.flip()
        # check for closing window
    while helpm:
        SCREEN.fill(BLACK)
        rtext1 = font2.render('Greetings, Admiral! While deploying press R to rotate. Click to fire on the enemy fleet.', True, WHITE) 
        rtext11 = rtext1.get_rect()
        rtext11.center = (WIDTH/2,HEIGHT/2)
        SCREEN.blit(rtext1,rtext11)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                helpm = False
                menu = True
        pygame.display.flip()

    


pygame.quit()
sys.exit()
