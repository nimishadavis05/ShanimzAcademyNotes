#id=
#name=
#age=

f=open("demo6.txt","r")
emp_id=[]
emp_name=[]
emp_age=[]
for lines in f:
	line=lines.rstrip("\n")
	value=line.split(",") #list 
	emp_id.append(value[0])
	emp_name.append(value[1])
	emp_age.append(value[2])
print("id=",emp_id)
print("name=",emp_name)
print("Age=",emp_age)



