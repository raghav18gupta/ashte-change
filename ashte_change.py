import pygame
import copy
from random import randint
from logics import *
from texts import *

print("Enter the numbers of players : ")
num_of_players = int(input())
set_players(num_of_players)

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
low_green = (100, 200, 255)
low_red = (255, 155, 100)
low_blue = (102, 204, 255)

board_coordinates = [ [  ] ]
#safe_cells = [ [0, 2], [4, 2], [2, 0], [2, 4], [2, 2] ]

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ashte Change")

game_width = int(800 * 0.6)
deck_width = width - game_width
width_gap = int(game_width//5)
height_gap = int(height//5)

game_surface = pygame.Rect( 0 , 0, game_width, height )
deck_surface = pygame.Rect( game_width, 0, deck_width, height )

steps = 0
selected_x = 0
selected_y = 0
selection_process = False
owner_in_process = 1

for i in range(0, 5):
	board_coordinates.append([])
	for j in range(0, 5):
		board_coordinates[i].append([ j*width_gap, i*height_gap, width_gap, height_gap ])

goti = pygame.Rect(board_coordinates[0][2][0], board_coordinates[0][2][1], width_gap//2, height_gap//2);
goti.center = ((board_coordinates[0][2][0]*2+width_gap)//2, (board_coordinates[0][2][1]+height_gap)//2)

def button(x, y, w, h, ac, pc):
	hoverMouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	buttonSurf = pygame.Rect(x, y, w, h)
	if( x+w > hoverMouse[0] > x and y+h > hoverMouse[1] > y ):
		screen.fill(ac, buttonSurf)
		if(click[0] == 1):
			return True
	else:
		screen.fill(pc, buttonSurf)
	return False

def draw_board():
	for i in range(0, 6):
		pygame.draw.line(screen, green, (i*width_gap, 0), (i*width_gap, height), 2)
		pygame.draw.line(screen, green, (0, i*height_gap), (game_width, i*height_gap), 2)

	for pairs in safe_cells:
		safe_x1_1 = board_coordinates[pairs[0]][pairs[1]][0]
		safe_y1_1 = board_coordinates[pairs[0]][pairs[1]][1]
		safe_x2_1 = board_coordinates[pairs[0]][pairs[1]][0] + width_gap
		safe_y2_1 = board_coordinates[pairs[0]][pairs[1]][1] + height_gap
		safe_x1_2 = board_coordinates[pairs[0]][pairs[1]][0]
		safe_y1_2 = board_coordinates[pairs[0]][pairs[1]][1] + height_gap
		safe_x2_2 = board_coordinates[pairs[0]][pairs[1]][0] + width_gap
		safe_y2_2 = board_coordinates[pairs[0]][pairs[1]][1]
		pygame.draw.line(screen, green, (safe_x1_1, safe_y1_1), (safe_x2_1, safe_y2_1), 2)
		pygame.draw.line(screen, green, (safe_x1_2, safe_y1_2), (safe_x2_2, safe_y2_2), 2)

	#screen.fill(black, goti)
	global selected_x, selected_y, owner_in_process
	mouse = pygame.mouse.get_pos()
	clicked_cell = pygame.mouse.get_pressed()
	for i in range(0, 5):
		for j in range(0, 5):
			#cell_x = j*width_gap
			#cell_y = i*height_gap
			cell_x = board_coordinates[i][j][0]
			cell_y = board_coordinates[i][j][1]
			if(cell_x + width_gap > mouse[0] > cell_x and cell_y + height_gap > mouse[1] > cell_y):
				if( clicked_cell[0] == 1 ):
					selected_y = mouse[0]//width_gap
					selected_x = mouse[1]//height_gap
					#owner_in_process = board_cell[selected_x][selected_y]
				active_cell = pygame.Rect(cell_x, cell_y, width_gap, height_gap)
				screen.fill(low_red, active_cell)

def draw_gotis():
	for i in range(0, 5):
		for j in range(0, 5):
			if(board_cell[i][j] != 0):
				goti_x = board_coordinates[i][j][0]
				goti_y = board_coordinates[i][j][1]
				goti = pygame.Rect( goti_x, goti_y, width_gap//10, height_gap//10 )
				goti.center = ( (goti_x *2 + width_gap )//2, (goti_y*2 + height_gap)//2 )
				screen.fill(p_color[board_cell[i][j] - 1], goti)

def draw_deck():
	TextSurface = arial.render("Turn : ", False, blue )
	screen.blit(TextSurface, ( ( game_width + int(deck_width*0.1) ) , int(height * 0.1) ))

	global steps, selection_process
	clicked = button(game_width + int(deck_width*0.4), int(height * 0.1), 100, 40, blue, green)
	if(clicked):
		steps = get_random_steps()
		selection_process = True

while True:
	for event in  pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	screen.fill(white, game_surface)
	screen.fill(low_blue, deck_surface)

	print("Player", owner_in_process, " turn ...")

	if(selection_process and selected_x != -1 and selected_y != -1):
		print(board_cell[selected_x][selected_y], owner_in_process)
		if(board_cell[selected_x][selected_y] == owner_in_process):
			prev_x = selected_x
			prev_y = selected_y
			#board_cell[selected_x][selected_y] = 0
			selected_x, selected_y = after_transition(selected_x, selected_y , steps)
			if(board_cell[selected_x][selected_y] != 0):
				print("You got to pass that ! Sorry.")
				back_to_home = board_cell[selected_x][selected_y]-1
				tod_status[owner_in_process-1] = True
				board_cell[selected_x][selected_y] = owner_in_process
				board_cell[ safe_cells[back_to_home][0] ][ safe_cells[back_to_home][1] ] = back_to_home+1
				board_cell[prev_x][prev_y] = 0
				steps = 4
				#selected_x = prev_x
				#selected_y = prev_y
			else:
				board_cell[selected_x][selected_y] = owner_in_process
				board_cell[prev_x][prev_y] = 0
			if (steps != 4 and steps != 8):
				owner_in_process += 1
			selection_process = False
			if(owner_in_process > num_of_players):
				owner_in_process = 1
		else:
			print("Not your turn !")
	else:
		selected_x = selected_y = -1


	draw_board()
	draw_gotis()
	draw_deck()

	pygame.display.update()