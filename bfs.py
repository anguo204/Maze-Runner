import queue
class node:
    def __init__(self,x,y,prv):
        self.nodex = x
        self.nodey = y
        self.prvnode = prv

def up(x , y):
    a = x
    b = y
    if(x>0):
        return a-1 , b
    return None
def down(x,y,n):
    a = x
    b = y
    if(x<n-1):
        return a+1 ,b
    return None
def right(x,y,n):
    a = x
    b = y
    if(y<n-1):
        return a , b+1
    return None
def left(x,y):
    a = x
    b = y
    if(y>0):
        return a , b-1
    return None
def vt(visited , xtemp , ytemp):
    for q_item in visited.queue:
        if(q_item.nodex == xtemp and q_item.nodey == ytemp):
            return True
    return False

def inque(q , x ,y):
    for q_item in q.queue:
        if(q_item.nodex == x and q_item.nodey == y):
            return True
    return False
def add(q, start , arr , n, visited):
    x = start.nodex
    y = start.nodey
    prvx = -1
    prvy = -1

    if(start.prvnode != None):
        prvx = start.prvnode.nodex
        prvy = start.prvnode.nodey
    print( str(prvx) + " " + str(prvy) + " "+ str(x) + " " + str(y))
    xtmp = 0
    ytmp = 0
    a = 0
    #print(y)
    if( up(x,y) != None):
        xtmp, ytmp = up(x,y)
        #print(str(xtmp) + " " + str(ytmp))
        if(( xtmp != prvx or ytmp != prvy) and arr[xtmp][ytmp] != 0 and inque(q, xtmp , ytmp) == False and vt(visited , xtmp , ytmp) == False):
            temp = node(xtmp,ytmp,start)
            if( temp != None):
                q.put(temp)
                a = 1
    if( down(x,y,n) != None):
        xtmp, ytmp = down(x,y,n)

        if( (xtmp != prvx or ytmp != prvy) and arr[xtmp][ytmp] != 0 and inque(q, xtmp , ytmp) == False and vt(visited , xtmp , ytmp) == False):
            print(str(xtmp) + " " + str(ytmp))
            temp = node(xtmp,ytmp,start)
            if( temp != None):
                q.put(temp)
                a = 1
    if( left(x,y) != None):
        xtmp, ytmp = left(x,y)
        #print(str(xtmp) + " " + str(ytmp))
        if(( xtmp != prvx or ytmp != prvy) and arr[xtmp][ytmp] != 0  and inque(q, xtmp , ytmp) == False and vt(visited , xtmp , ytmp) == False):
            temp = node(xtmp,ytmp,start)
            if( temp != None):
                q.put(temp)
                a =1
    if(right(x,y,n) != None):
        xtmp, ytmp = right(x,y,n)
        #print(str(xtmp) + " " + str(ytmp))
        if( (xtmp != prvx or ytmp != prvy) and arr[xtmp][ytmp] != 0  and inque(q, xtmp , ytmp) == False and vt(visited , xtmp , ytmp) == False):
            temp = node(xtmp,ytmp,start)
            if( temp != None):
                q.put(temp)
                a=1
    #print(a)
    return a
def bfs(arr,n):
    start = node(0,0,None)
    temp = start
    q = queue.Queue(maxsize=n*n)
    visited = queue.Queue(maxsize=n*n)
    add(q,start, arr , n , visited)

    visited.put(start)
    max = 0
    absmax = 0
    #for q_item in q.queue:
        #print (str(q_item.nodex) + " " + str( q_item.nodey))
    while((temp.nodex!=n-1 or temp.nodey != n-1) and q.empty() != True  ):
        temp = q.get()

        for q_item in q.queue:
            max = max +1
            #print (str(q_item.nodex) + " " + str( q_item.nodey))
        #print(str(temp.nodex) + " " + str( temp.nodey))
        if( max > absmax):
            absmax = max
        max = 0
        print("next")
        a = add(q,temp, arr , n, visited)
        visited.put(temp)
        print(a)


    #print(str(temp.nodex) + " " +str(temp.nodey))

    if( temp.nodex ==n-1 and temp.nodey == n-1  ):
        return temp, visited , absmax
    print(q.empty())
    return None , visited , absmax
