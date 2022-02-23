#recursive character

text="ABBCCC"
dict={}
for c in text: #A B B
	if(c not in dict): #A B B false
		dict[c]=1 #dict[A]=1 dict[B]=1 
	else:
		print("the first recursive char:",c) # B
		break