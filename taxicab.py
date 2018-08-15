import sys

blocks=  "R4, R1, L2, R1, L1, L1, R1, L5, R1, R5, L2, R3, L3, L4, R4, R4, R3, L5, L1, R5, R3, L4, R1, R5, L1, R3, L2, R3, R1, L4, L1, R1, L1, L5, R1, L2, R2, L3, L5, R1, R5, L1, R188, L3, R2, R52, R5, L3, R79, L1, R5, R186, R2, R1, L3, L5, L2, R2, R4, R5, R5, L5, L4, R5, R3, L4, R4, L4, L4, R5, L4, L3, L1, L4, R1, R2, L5, R3, L4, R3, L3, L5, R1, R1, L3, R2, R1, R2, R2, L4, R5, R1, R3, R2, L2, L2, L1, R2, L1, L3, R5, R1, R4, R5, R2, R2, R4, R4, R1, L3, R4, L2, R2, R1, R3, L5, R5, R2, R5, L1, R2, R4, L1, R5, L3, L3, R1, L4, R2, L2, R1, L1, R4, R3, L2, L3, R3, L2, R1, L4, R5, L1, R5, L2, L1, L5, L2, L5, L2, L4, L2, R3"


directions = blocks.split(", ")  #split string by comma into a list


						
orientation = ("N")      

#for instruction in directions: 
#	turn, dist = instruction[0], int(instruction[1:])
	
	
 	
							#course it refers to North, East... and direct to 'R'+Number anD 'L'+  number
def next_dir(course, direct):
	y_dir = 0
	x_dir = 0
	coordinates = set()
	for i in direct:
		turn_LR, dist = i[0], int(i[1:])
		if turn_LR == "L":			#If turn we check the orientation
			if  course == "N":
				course = "W"
				for x in xrange(1,dist+1): # (start, stop)
					x_dir -= 1
					find_coord((x_dir,y_dir), coordinates)
			
				
			elif course == "E":
				course = "N"
				for x in range(1,dist+1):
					y_dir += 1
					find_coord((x_dir,y_dir), coordinates)
				
			
			elif course == "S":
				course = "E"
				for x in range(1,dist+1):
					x_dir += 1
					find_coord((x_dir,y_dir), coordinates)
				
			
			elif course == "W":
				course = "S"
				for x in range(1,dist+1):
					y_dir -= 1
					coordinates.add((x_dir,y_dir))
				#y_dir = y_dir - 1 
			
		if turn_LR == "R":
			if course == "N":
				course ="E"
				for x in range(1,dist+1):
					x_dir += 1
					find_coord((x_dir,y_dir), coordinates)
				
			
			elif course == "E":
				course = "S"
				for x in range(1,dist+1):
					y_dir -= 1
					find_coord((x_dir,y_dir), coordinates)
				
			
			elif course == "S":
				course = "W"
				for x in range(1,dist+1):
					x_dir -= 1
					find_coord((x_dir,y_dir), coordinates)
				
			elif course == "W":
				course = "N"
				for x in range(1,dist+1):
					y_dir += 1
					find_coord((x_dir,y_dir), coordinates)
				
				
		new = (x_dir, y_dir)
		#print coordinates
		print new, turn_LR, dist, course
		"""if new not in coordinates:
			coordinates.add(new)
		else: 	
			#print turn_LR, dist
			#print coordinates
			break """ 
	return x_dir, y_dir
					
def find_coord(local_new, local_coordinates):
	if local_new not in local_coordinates:
		local_coordinates.add(local_new)
	else:
		dist = int(abs(local_new[0])+abs(local_new[1]))
		print "The headquarters is " + str(dist) + " blocks away"
		sys.exit()
	


x_dist, y_dist = next_dir(orientation, directions)
#print x_dist, y_dist


def best_path(x_dist, y_dist):
	return int(abs(x_dist)+abs(y_dist))
	
blocks_away = best_path(x_dist, y_dist)
print "The headquarters is " + str(blocks_away) + " blocks away"
	

	
		
		
		

		
		
		
		
