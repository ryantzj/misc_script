list_x = [-2,-1,1,2,3,4]
list_y = [-6,-5,-4,-3,-2,1,2]
list_z =[]

for item_x in list_x:
	for item_y in list_y:
		list_z.append(item_x-item_y)

big =  max(list_z)
small =  min(list_z)

if big < 2 and small > -10:
	print "answer is a"
elif big < 8 and small > 4:
	print "answer is b"
elif big < 12 and small > -6:
	print "answer is c"
elif big < 6 and small > -3:
	print "answer is d"
elif big < 3 and small > 1:
	print "answer is e"


