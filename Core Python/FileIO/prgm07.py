f=open("demo7.txt","r")
dict={}
for lines in f:
	movies=lines.rstrip("\n").split(",")
	rate=movies[3] #rating
	movie=movies[1] #movie name
	if(movie not in dict):
		dict[movie]=rate
	else:
		dict[movie]=rate
for k,v in dict.items():
	print(k,",",v)
lst=[]
for k,v in dict.items():
	lst.append((v,k))
	lst=sorted(lst,reverse=True)
print(lst)
print(lst[0])	
