#queue implemention using list
queue=[]
def enqueue():
    element=int(input("enter the element"))
    queue.append(element)
    print(queue)
def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e=queue.pop(0)
        print("removed element:",e)
def display():
    print(queue)
while True:
    print("select option 1.enqueue 2.dequeue 3.show 4.quit")
    choice=int(input())
    if choice==1:
       enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("choose the correct option")
