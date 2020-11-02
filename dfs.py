import sys
visited = []
stack = []
lengthvisited = []
sys.setrecursionlimit(5000)
class node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
temp = node(0,0)
def left(x,y,n):
    if((x > 0) and (x-1,y) not in visited ) :
        return x-1, y

def right(x,y,n):
    if((x < n-1) and (x+1,y) not in visited ):
        return x+1, y

def up(x,y,n):
    if((y > 0) and (x,y-1) not in visited ):
        return x, y-1

def down(x,y,n):
    if ((y < n-1) and (x,y+1) not in visited ):
        return x, y+1

def dfs(start,arr,n):
    x = start.x
    y = start.y
    if(left(x,y,n)!=None):
        tempx,tempy = left(x,y,n)
        if arr[tempx][tempy] != 0:
            stack.append((tempx,tempy))
        #print(stack)
    if(right(x,y,n)!=None):
        tempx,tempy = right(x,y,n)
        if arr[tempx][tempy] != 0:
            stack.append((tempx,tempy))
        #print(stack)
    if(up(x,y,n)!=None):
        tempx,tempy = up(x,y,n)
        if arr[tempx][tempy] != 0:
            stack.append((tempx,tempy))
        #print(stack)
    if(down(x,y,n)!=None):
        tempx,tempy = down(x,y,n)
        if arr[tempx][tempy] != 0:
            stack.append((tempx,tempy))
        #print(stack)
    visited.append((start.x,start.y))
    if len(stack) != 0:
        temp.x,temp.y = stack.pop()
        if (temp.x,temp.y) == (n-1,n-1):
            visited.append((temp.x,temp.y))
            print("found path")
            lengthvisited.append(len(visited))
        else:
            dfs(temp,arr,n)
    else:
        print("No Path Found!")
        lengthvisited.append(len(visited))
