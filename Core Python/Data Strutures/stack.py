#Ques : Perform stack operations , - push,pop in a list and Follow LIFO principle
size=int(input("Enter stack size:")) #5
stk=[]
top=0
def push(element): # element - argument
    global top
    if(top>=size):
        print("stack is full")
    else:
        stk.append(element) #apppend /inserted to stk
        top+=1 #top increment
        print("value inserted")
def pop():
    global top
    if(top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top-=1
        print("element removed")
def display():
    print("Stack element are: ")
    for i in range(0,top):
        print(stk[i])

n=1
while(n!=0): #n=1
    option=int(input("Choose Operations :Please 1.Push  2. POP 3.Display"))
    if(option==1):
        element=int(input("Enter element"))
        push(element) #calling push() , argument - element 
    elif(option==2):
        pop() # callingpop()
    elif(option==3):
        display() 
    n=int(input("Press 0 to exit , 1 to continue!!"))

