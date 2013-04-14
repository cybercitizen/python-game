import pygame, sys, random, time
from pygame.locals import *
from random import randint	
pygame.init()
mainClock=pygame.time.Clock

#COLORS
SKYBLUE=(238,232,170)
CORAL=(255,127,80)
BLACK=(0,0,0)
WHITE=(255,255,255)
TAN=(210,180,140)
GREY=(105,105,105)
BROWN=(188,143,143)
RED=(200,0,0)

#VARIABLES
NOW=time.time()+5
START=time.time()+2
T_NOW=time.time()+1
T_COUNT=0
moveRight1=False
moveLeft1=False
WINDOW_WIDTH=800
WINDOW_HEIGHT=600
MOVESPEED=1
FIRE_START=0
SCORE=0
ROCK_COUNT=0
moveRight=False
moveLeft=False
fire=False
play=True
FIRED=False
MIN=0

def drawText(text,color, font, surface, x, y):
	textobj = font.render(text, 1,color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

basicFont=pygame.font.SysFont('BahamasHeavy', 35)
messageFont=pygame.font.SysFont('BahamasHeavy', 15)
field=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,32)
pygame.display.set_caption('Tank')
player=pygame.Rect(0,530,60,30)
tank1=pygame.image.load('tank1.jpg')
tank2=pygame.image.load('tank2.jpg')
rock=pygame.image.load('rock.jpg')
ROCK=[]

for i in range(20):
	ROCK.append(pygame.Rect(randint(5,790),randint(75,460),20,20))

while True:
	if T_NOW<time.time():
		T_COUNT+=1
		T_NOW=time.time()+1
	for event in pygame.event.get():
		if event.type==QUIT or T_COUNT%120==121:
			field.fill(BLACK)
			drawText('Your Score is: '+str(SCORE),BROWN, basicFont, field,230,280)
			pygame.display.update()
			time.sleep(2)
			pygame.quit()
			sys.exit()
		if event.type==KEYDOWN:
			if event.key==K_RIGHT:
				moveRight=True
				moveLeft=False
			if event.key==K_LEFT:
				moveRight=False
				moveLeft=True
			if event.key==K_SPACE:
				fire=True
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				field.fill(BLACK)
				drawText('Your Score is: '+str(SCORE),BROWN, basicFont, field,230,280)
				pygame.display.update()
				time.sleep(2)
				pygame.quit()
				sys.exit()
			if event.key==K_RIGHT:
				moveRight=False
			if event.key==K_LEFT:
				moveLeft=False
			if event.key==K_SPACE:
				fire=False
	if moveRight and player.right<830:
		player.right+=MOVESPEED
	if moveLeft and player.left>0:
		player.left-=MOVESPEED
	if play==True:
		while START>=time.time():
			drawText('WELCOME!!!',SKYBLUE, basicFont, field,305,150)
			drawText('Press ESCAPE any time to Exit!!!',TAN, basicFont, field,140,210)
			drawText('Use ARROW KEYS to Navigate!!',BROWN, basicFont, field,145,280)
			drawText('Use SPACE to Fire!!!',BROWN, basicFont, field,245,350)
			drawText('You Have 2 Minutes!!!',RED, basicFont, field,225,420)
			pygame.display.update()
		play=False
		time.sleep(2)
						
	field.fill(BLACK)
	pygame.draw.rect(field,BROWN,(0,0,800,70))
	drawText('Score: '+str(SCORE),CORAL, basicFont, field,105,8)
	drawText('Time: '+str(T_COUNT%120) ,CORAL, basicFont, field,505,8)
	drawText('Press Escape To Exit!!',RED, messageFont, field,300,40)
	field.blit(tank1,player)
	field.blit(rock,ROCK[i])
	pygame.display.update()
	time.sleep(0.001)
	if fire:
		field.blit(tank2,player)
		FIRE_START=player.left+15
		pygame.draw.polygon(field,BROWN,((FIRE_START,530),(FIRE_START-3,50),(FIRE_START+3,50),(FIRE_START,530)))
		pygame.display.update()
		time.sleep(0.1)
		if FIRE_START>ROCK[i].left and FIRE_START <ROCK[i].right:
			pygame.draw.rect(field,BLACK,((0,50),(800,500)))
			pygame.display.update()
			i=randint(0,19)
			SCORE+=1

