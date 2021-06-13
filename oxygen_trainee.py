trainee = [[],[],[],[]]
for i in range(3):
	for j in range(3):
    		trainee[i].append(int(input()))
    		if (trainee[i][-1]) not in range(1,101):
        			print("invalid input")
for i in range(3):
	trainee[3].append((trainee[2][i]+trainee[1][i]+trainee[0][i])//3)
maximum = max(trainee[3])
for i in range(3):
	if trainee[3][i] < 70 :
    		print("Trainee {0} is unfit".format(i+1))
	elif trainee[3][i] == maximum:
    		print("Trainee Number: ",i+1)
