with open("triangles.txt") as t:
	count_triangles = 0 
	for line in t:
		row = line.split()
		side1_2 = int(row[0]) + int(row[1])
		side2_3 = int(row[1]) + int(row[2])
		side1_3 = int(row[0]) + int(row[2])
		if ((side1_2 > (int(row[2]))) and (side2_3 > (int(row[0]))) and (side1_3 > (int(row[1])))):
			count_triangles = count_triangles + 1
	print count_triangles			
