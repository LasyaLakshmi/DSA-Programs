class stack:
    def __init__(self,cap):
        self.cap = cap
        self.top=-1
        self.a = [0]*cap
    def push(self,x):
        if self.top>=self.cap-1:
            print("\n stack is overflow")
            return False
        self.top += 1
        self.a[self.top] = x
        return True 
    def pop(self,x):
        if self.top <0:
            print("\n stack is underflow")
            return False
        
        self.top-=1
        