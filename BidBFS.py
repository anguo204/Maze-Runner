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
def bidbfs(arr,n):
    max = 0
    absmax = 0
    start = node(0,0,None)
    end = node(n-1 , n-1 , None)
    temp = start
    temp1=end
    q = queue.Queue(maxsize=n*n)
    visited = queue.Queue(maxsize=n*n)
    visited1 = queue.Queue(maxsize=n*n)
    q1 = queue.Queue(maxsize= n*n)
    add(q,start, arr , n , visited)
    add(q1, end , arr , n , visited1)
    visited.put(start)
    visited1.put(end)
    #for q_item in q.queue:
        #print (str(q_item.nodex) + " " + str( q_item.nodey))
    while( q.empty() != True and q1.empty() !=True  ):
        temp = q.get()
        temp1 = q1.get()
        if( temp.nodex == temp1.nodex and temp.nodey == temp1.nodey):
            return temp , temp1 ,visited.qsize() + visited1.qsize() , absmax
        """
        for q_0 in q.queue:
            for q_1 in q1.queue:
                if(q_0.nodex == q_1.nodex and q_0.nodey == q_1.nodey):
                    return q_0 , q_1
                if(q_0.nodex == temp1.nodex and q_0.nodey == temp1.nodey):
                    return q_0, temp1
                if( q_1.nodex == temp.nodex and q_1.nodey == temp.nodey):
                    return temp , q_1
        """
        for q_0 in q.queue:
            max = max +1
            if(q_0.nodex == temp1.nodex and q_0.nodey == temp1.nodey):
                return q_0, temp1,visited.qsize() + visited1.qsize() , absmax
        for v_0 in visited.queue:
            if(v_0.nodex == temp1.nodex and v_0.nodey == temp1.nodey):
                return v_0, temp1,visited.qsize() + visited1.qsize() , absmax
        for q_1 in q1.queue:
            max = max +1
            if(q_1.nodex == temp.nodex and q_1.nodey == temp.nodey):
                return temp, q_1,visited.qsize() + visited1.qsize() , absmax
        for v_1 in visited1.queue:
            if(v_1.nodex == temp.nodex and v_1.nodey == temp.nodey):
                return temp,v_1,visited.qsize() + visited1.qsize() , absmax
        if( max > absmax):
            absmax = max
        max = 0
        #print(str(temp.nodex) + " " + str( temp.nodey))
        #print("next")
        if(temp1 != None):
            b = add(q1, temp1 , arr, n , visited1)
            visited1.put(temp1)
        if(temp != None):
            a = add(q,temp, arr , n, visited)
            visited.put(temp)
        print(a)


    #print(str(temp.nodex) + " " +str(temp.nodey))
    """
    if( (temp.nodex ==n-1 and temp.nodey == n-1)   ):
        return temp
    """
    print(q.empty())
    return 0 , 0 , visited.qsize() + visited1.qsize() , absmax
