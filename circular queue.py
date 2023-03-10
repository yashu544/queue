class CircularQueue:
    def __init__(self,size):
        
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rare=-1

    def enqueue(self,data):
        if ((self.rare+1)%self.size==self.front):
            print("queue is full\n")
        elif(self.front==-1):
            self.front=0
            self.rare=0
            self.queue[self.rare]=data
        else:
            self.rare=(self.rare+1)%self.size
            self.queue[self.rare]=data
    def dequeue(self):
        if (self.front==-1):
            print("queue is full")
        elif (self.front==self.rare):
            temp=self.queue[self.front]
            self.front=-1
            self.rare=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("Queue is empty")
        elif(self.rare>=self.front):
            print("element in the circular queue:")
            for i in range(self.front,self.rare+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("elements in circular queue are:")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rare+1):
                print(self.queue[i],end=" ")
            print()
        if((self.rare+1)%self.size==self.front):
            print("Queue is full")
ob=CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print("deleted value=",ob.dequeue())
print("deleted value=",ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
            

    
