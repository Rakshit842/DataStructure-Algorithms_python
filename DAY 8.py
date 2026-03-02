class stack: 
    def __init__(self, mycapacity):
        self.top = -1
        self.capacity = mycapacity
        self.stackArray = [None]*mycapacity

    def push(self, mydata): 
        if self.top == self.capacity-1:
            print("stack overflow")
            return
        
        self.top+=1
        self.stackArray[self.top] = mydata

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return
        
        mydata = self.stackArray[self.top]
        self.top -= 1       
        return mydata
    
    def peek(self):
        if self.top == -1:
            return     
        return self.stackArray[self.top]
    
    def isEmpty(self): 
        if self.top == -1: 
            return True
        return False
    
    def isFull(self):
        if self.top == self.capacity -1:
            return True
        return False
    
myStack = stack(5) 

print(myStack.isEmpty())
print(myStack.isFull())

myStack.push(10)
myStack.push(12)
myStack.push(13)
myStack.push(14)
myStack.push(15)
myStack.push(9)

print(myStack.peek())

myStack.pop()