f=open("demo3.txt","r")
words=[]
for lines in f:
	line=lines.rstrip("\n") #iam nimisha from shanimz academy
	word=line.split(" ") #hello,welcome,to
	for i in word:
		words.append(i) #word =['hello','welcome ']
print(words) #words
for j in words:
	print(j)		