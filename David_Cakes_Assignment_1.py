class Bakery:
    def __init__(self):
        self.stack=[]
        self.b=[]
    def cake(self,a):
        stack=self.stack
        b=self.b
        for list in a:
            for number in list:
                b.append(number)
        for i in range(len(b)):
            if b[i]==1:
                if len(stack)==0:
                    print("No Cake")
            elif b[i]==2:
                stack.append(b[i+1])
            if b[i]==1:
                if len(stack)>0:
                    print(stack.pop())


obj=Bakery()
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
obj.cake(a)
