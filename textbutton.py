import sys
import pygame
from pygame.locals import *

pygame.init()
gameMode_audio = pygame.mixer.Sound('gameMoswAudio.mp3')
gameMode_audio.play()

screen_width = 1000
screen_height = 800
BACKGROUND = pygame.image.load('img/background.png')
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird Game Mode')
FPS = 60
fpsClock = pygame.time.Clock()
font = pygame.font.Font('04B_19.ttf', 65)

#define colours

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False
counter = 0

class button():
		
	#colours for button and text
	button_col = (78, 192, 202)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = black
	width = 230
	height = 130

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):
        
		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        
		return action


hand = button(170, 200, 'Hand')
quit = button(370, 490, 'Quit?')
normal = button(570, 200, 'Normal')

run = True
while run:

	screen.blit(BACKGROUND, (0, 0))

	if hand.draw_button():
		exec(open('flappybird.py').read())
		counter = 0
	if quit.draw_button():
		sys.exit()
       
	if normal.draw_button():
		exec(open('normal_flappy.py').read())
		counter += 1

	

	


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()


pygame.quit()