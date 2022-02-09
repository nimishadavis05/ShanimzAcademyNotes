# dictionary created or defined
emp={"id":101,"name":"nimisha","salary":56000} 
# print emp
print(emp)

# print the individual value using key
print(emp["name"])
print(emp["salary"])

# add a new field -   gender:female
emp["gender"]="female"
print(emp)

# salary updated to 60000
emp["salary"]+=4000
# a+=1
# a=a+1
print(emp)
# key present or not
print("name" in emp)
