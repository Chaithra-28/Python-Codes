x=int(input('enter x co\n'))
y=int(input('enter y co\n'))
z=int(input('enter z co\n'))
n=int(input('enter n co\n'))
output_list=[]
for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			if i+j+k!=n:
				arr=[i,j,k]
				output_list.append(arr)
output_list.sort()
print(output_list)
