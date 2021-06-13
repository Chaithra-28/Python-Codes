'''#counts numb of crt bracket sequences
s=input()
open=[]
close=[]
for i in s:
	if i=='(':
		open.append(i)
	elif i==')':
		close.append(i)
if len(open)>len(close):
	print(len(close))
elif len(close)>len(open):
	print(len(open))
elif len(close)==len(open):
	print(len(open))
'''

#result gives numb of shifts in order to obtain crt bracket sequences

def solve(s):
	open=0
	close=0
	res=0
	for i in s:
		if(i=='('):
			open+=1
		else:
			open-=1

		if (open<close):
			close=open
			res=0

		if (close==open):
			res+=1

	if open:
		return 0
	else:
		return res

s= input()
print(solve(s))