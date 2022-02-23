text="hello hai hello hi hai hello"
print(text)
print(type(text))
words=text.split(" ") #we will get a list
print(words)
# ['hello', 'hai', 'hello', 'hi', 'hai', 'hello']
print(type(words))
dict={}
for word in words:  #hello
	if(word not in dict): #hello 
		dict[word]=1 
	else:
		dict[word]+=1 #dict["hello"]+=1
print(dict)	

	# {'hello':3,'hai':2,'hi':1}

