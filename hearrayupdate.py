'''
t=int(input('numb of test cases\n'))
for _ in range(t):
	N,K= list(map(int,input('enter n and k\n').split()))
	arr=[int(i) for i in input().split()][:N]
	print(arr)
	min_time,min_ele= 0,min(arr)
	while(min_ele<=K):
		min_ele+=1
		min_time+=1
	print(min_time)
'''
'''
t=int(input('numb of test cases\n'))
for _ in range(t):
	N,K= list(map(int,input('enter n and k\n').split()))
	arr=[int(i) for i in input().split()][:N]
	mini=min(arr)
	if mini<K:
		print(K-int(mini))
	else:
		print(0)
'''

	

