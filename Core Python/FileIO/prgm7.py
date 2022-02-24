f=open("demo7.txt","r")
dict={}
for lines in f:
	movies=lines.rstrip("\n").split(",")
	# print(movies)
	year=movies[2]
	if(year not in dict):
		dict[year]=1
	else:
		dict[year]+=1
print(dict)

#which year? 
lst=[]
for k,v in dict.items():
	lst.append((v,k))
print(lst)			
sortedlist=sorted(lst,reverse=True)
print(sortedlist)
print(sortedlist[0])










