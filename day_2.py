KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
KEYPAD2 = [[0, 0 ,0 ,0 , 0, 0, 0],[0, 0, 0, 1, 0, 0, 0], [0, 0, 2, 3, 4, 0, 0], [0, 5 ,6, 7, 8, 9, 0], [0, 0, "A", "B" ,"C" ,0, 0], [0, 0 ,0 ,"D", 0, 0, 0],[0, 0 ,0 ,0, 0, 0, 0]]

print ("Part 1")
with open("instruction_toy.txt") as instruction:
	coordinates = []
	x = 1
	y = 1
	for inst in instruction:
		
		#aux_x = 1
		#aux_y = 1
		for i in inst:
			if i == 'U':
				y = y - 1
				if(y >= 0 and y <= 2):
					coordinates.append((y,x))
				else:
					y = y + 1
					
			elif i == 'D':
				y = y + 1
				if (y>= 0 and y <= 2): 
					coordinates.append((y,x))
				else:
					y = y - 1
		
			elif i == 'L':
				x = x - 1
				if (x >= 0 and x <= 2):
					coordinates.append((y,x))
				else: 
					x = x + 1
					
			elif i == 'R':
				x = x + 1
				if((x >= 0) and (x <= 2)):
					coordinates.append((y,x))
				else:
					x = x - 1
					
					
		#	print (y,x), i, KEYPAD[y][x]
		c = coordinates[-1]
		print KEYPAD[c[0]][c[1]], c
		print coordinates[-1]
print
print ("Part 2")
print
with open("instruction_toy.txt") as instruction:
	x = 1
	y = 2 
	coordinates = [(y,x)]
	for inst in instruction:
		print inst
		for i in inst:
			print i
			if i == 'U':
				y = y - 1
				if KEYPAD2[y][x] != 0:
					coordinates.append((y,x))
				else:
					y = y + 1
					
			elif i == 'D':
				y = y + 1
				
				if KEYPAD2[y][x] != 0: 
					coordinates.append((y,x))
				else:
					y = y - 1
					

			elif i == 'L':
				x = x - 1
				if KEYPAD2[y][x] != 0:
					coordinates.append((y,x))
				else: 
					x = x + 1
					
			elif i == 'R':
				x = x + 1
				if KEYPAD2[y][x] != 0:
					coordinates.append((y,x))
				else:
					x = x - 1
					
					
			print (y,x), i, KEYPAD2[y][x]
		a = coordinates[-1]
		print KEYPAD2 [a[0]][a[1]], a
		print coordinates[-1]



#def check_limits(y_local,x_local):
#		y_local >= 0 and y_local <= 2
#		x_local >= 0 and x_local <= 2
			
