#create a stack from list
mystack=list()

#stack is empty or not
def empty(mystack):
    if len(mystack)==0:
        return True
    else:
        return False
    
#add element in stack
def stackpush(mystack,element):
    mystack.append(element)
    option()

#remove element from stack
def stackpop(mystack):
    if empty(mystack):
        print("underflow")
        return None
    else:
        return (mystack.pop())

#size of stack
def size(mystack):
    return len(mystack)

#top of stack
def top(mystack):
    if empty(mystack):
        print("khali stack")
        return None
    else:
        x=len(mystack)
        data=mystack[x-1]
        return data

#all elements show of stack
def show(mystack):
    x=len(mystack)
    if empty(mystack):
        print("khali stack")
        option()
    else:
        print("list current element = ")
        for i in range(x-1,-1,-1):
            print(mystack[i])
        option()



#choose all operation on stack
def option():
    print("===================================================================================================")
    print("push element for = 1\npop element for 2\nshow whole list for 3\nfind top of list for 4\nfind list size for 5 ")
    print("===================================================================================================")
    ch=int(input("enter the choice = "))
    

    if ch==1:
        data=input("enter the element = ")
        stackpush(mystack,data)
    
    elif ch==2:
        stackpop(mystack)
        option()

    elif ch==3:
        show(mystack)

    elif ch==4:
        data=top(mystack)
        print(data)
        option()
    
    elif ch==5:
        s=size(mystack)
        print(s)
        option()

    else:
        print("wrong option choose")

option()















