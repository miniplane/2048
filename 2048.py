import random, time

def move_helper(current_line):
	new_line = []
	j = 0
	for i in current_line:
		if i == 0:
			continue
		if i==j:
			new_line[-1]=i*2
			i=0
		else:
			new_line.append(i)
		j=i
	while len(new_line) < 4:
		new_line.append(0)
	if current_line!=new_line:
		global same
		same = False
	return new_line
#-431 -1000
def move_right():
	for i in range(4):
		a = i*4-1
		if a < 0:
			a=None
		line_slice = slice(i*4+3, a, -1)
		field[line_slice] = move_helper(field[line_slice])

def move_left():
	for i in range(4):
		line_slice = slice(i*4, i*4+4, 1)
		field[line_slice] = move_helper(field[line_slice])

def move_up():
	for i in range(4):
		line_slice = slice(i, 4*4, 4)
		field[line_slice] = move_helper(field[line_slice])	

def move_down():
	for i in range(4):
		a = i-1
		if a < 0:
			a=None
		line_slice = slice(4*3+i, a, -4)
		field[line_slice] = move_helper(field[line_slice])


field = [0 for i in range(4*4)]

print ("Controls: Left: a, Right: d, Up: w, Down: \nGood Game!")

while True:
	empty_field = [e for e, i in enumerate(field) if i == 0]
	nextfield = random.choice(empty_field)
	field[nextfield] = random.choice([2, 2, 2, 4])

	for i in range (4):
		for j in range (4):
			print (str(field[((i*4)+j)]) + " ", end ="")
		print ()

	if (0 not in field):
		break

	while True:
		same = True
		direction = input("> ")
		if direction == "a":
			move_left()
		elif direction == "d":
			move_right()
		elif direction == "w":
			move_up()
		elif direction == "s":
			move_down()
		if same == False:
			break

	print ()

print ("Game over!")
