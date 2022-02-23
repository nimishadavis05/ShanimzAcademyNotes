#store to list

f=open("demo2.txt","r")  #file open , read
lst=[] #created an empty list
for num in f: #100\n101 102 103 104
	numbers=int(num.rstrip("\n")) #102
	lst.append(numbers) #102
print(lst)
print(sum(lst))
print(max(lst))
print(min(lst))