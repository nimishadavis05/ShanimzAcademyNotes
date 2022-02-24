#district wise covid details
#highest death rate

f=open("demo8.txt","r")
dict={}
for lines in f:
	data=lines.rstrip("\n").split(",")
	print(data)
	district=data[1]
	death=int(data[2])
	if(district not in dict):
		dict[district]=death
	else:
		dict[district]=death
print(dict)
for k,v in dict.items():
	print(k,",",v)
lst=[]
for k,v in dict.items():
	lst.append((v,k))
	lst=sorted(lst,reverse=True)			
print(lst)	
print(lst[0])