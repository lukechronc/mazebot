"""Ting by Lukas Chronc ----- Pro nekomercni pouziti ----"""
import maze
code = 'karimatka'
c = maze.Connect('lukechronc', code)

all = c.get_all()
#print(all[0])
x = c.x()
y = c.y()




cesta = []

while all[x][y] != 3:

	all[x][y] = 2
	
	if all[x + 1][y] != 2:
		cesta.append(x) 
		cesta.append(y)
		cesta.append('d')
		x = x + 1
	elif all[x][y + 1] != 2:
		cesta.append(x)
		cesta.append(y)
		cesta.append('s')
		y = y + 1	
	elif all[x - 1][y] != 2:
		cesta.append(x)
		cesta.append(y)
		cesta.append('a')		
		x = x - 1
	elif all[x][y - 1] != 2:
		cesta.append(x)
		cesta.append(y)
		cesta.append('w')
		y = y - 1
	else:
		cesta.pop()
		y = cesta.pop()
		x = cesta.pop()
		print('NOPE BIATCH')
while cesta:
	cesta.pop(0)
	cesta.pop(0)
	smer = cesta.pop(0)

	if smer == 'w':
		c.move('w')
	if smer == 'a':
		c.move('a')
		c.move('w')
		c.move('d')
	if smer == 's':
		c.move('d')
		c.move('d')
		c.move('w')
		c.move('d')
		c.move('d')
	if smer == 'd':
		c.move('d')
		c.move('w')
		c.move('a')
