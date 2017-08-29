from random import randint

board_cell = [ [ ] ]

players = 0
gotis = []
tod_status = []
safe_cells = [ [0, 2], [4, 2], [2, 0], [2, 4], [2, 2] ]
p1_color = (255, 255, 10)
p2_color = (255, 10, 255)
p3_color = (10, 255, 255)
p4_color = (1, 255, 10)
p_color = [ p1_color, p2_color, p3_color, p4_color ]

def set_players(n):
	players = n
	for i in range(0, n):
		tod_status.append(False)
	
	pl = 1
	for i in range(0, 5):
		board_cell.append([])
		for j in range(0, 5):
			board_cell[i].append(0)
	
	for i in range(0, n):
		for p_n in range(0, 4):
			board_cell[safe_cells[i][0]][safe_cells[i][1]] = pl
		pl += 1

def get_random_steps():
	a = randint(0, 1)
	b = randint(0, 1)
	c = randint(0, 1)
	d = randint(0, 1)
	sum = a+b+c+d
	if(sum == 4):
		return 8
	if(sum == 0):
		return 4
	return 4-sum

def change_pos(s_x, s_y):
	if(s_x == 0):
		if(s_y > 0):
			return s_x, s_y-1
		else:
			return 1, 0
	if(s_x == 4):
		if(s_y < 4):
			return s_x, s_y+1
		else:
			return 3, 4
	if(s_y == 0):
		if(s_x < 4):
			return s_x+1, s_y
		else:
			return 4, 1
	if(s_y == 4):
		if(s_x > 0):
			return s_x-1, s_y
		else:
			return 0, 3

def after_transition(x, y, steps):
	while(steps > 0):
		x, y = change_pos(x, y)
		steps -= 1
	return x, y