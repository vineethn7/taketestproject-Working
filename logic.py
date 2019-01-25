file1 = open("ques.txt", 'r')
lines=file1.readlines()
file1.close()
ques=[]
options=[]
ans=[]

for line in lines:
	if "Q:" in line:
		ques.append(line)

	if "opt" in line:
		options.append(line.replace('*',''))

	if "*" in line:
		ans.append(line)

for qu in ques:
	print(qu)
for op in options:
	print(op,end="")
for an in ans:
	print(an,end="")
print("\n")
i=0
quesBank={}
for qu in ques:
	quesBank[qu] = [options[x] for x in range(i,i+4)]
	i=i+4
print(quesBank)
for x in quesBank.items():
	print(x)
	print()
