state_one='''
 __ __
|R |  |
|__|__|
|  |D |
|__|__|
'''
print(state_one)
state_two='''
 __ __
|  |R |
|__|__|
|  |D |
|__|__|
'''
state_three='''
 __ __
|  |  |
|__|__|
|R | D|
|__|__|
'''
state_four='''
 __ __
|  |  |
|__|__|
|  | R|
|__|__|
'''
move=input("enter u,d,r,l\n")
if move=='r':
	print(state_two)
	move=input("enter u,d,r,l\n")
	if move=='d':
		print(state_four)
		print("cleaned")
elif move=='d':
	print(state_three)
	move=input("enter u,d,r,l\n")
	if move=='l':
		print(state_four)
		print("cleaned")
	



