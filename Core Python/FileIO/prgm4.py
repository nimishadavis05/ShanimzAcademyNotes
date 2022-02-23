#case converstion

f=open("demo4.txt","r")
words=[]
for lines in f:
	line=lines.rstrip("\n")
	word=line.split(" ")
	for j in word:
		words.append(j.upper())
print(words)	