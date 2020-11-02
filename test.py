from graphics import *
import numpy as np
import math
import bfs
import BidBFS
import Astar
import dfs
import csv
import random
"""
win = GraphWin("My maze", 500, 500)
shape = Rectangle(Point(80,0), Point(120,40) )
shape.setOutline("red")
shape.setFill("red")
shape.draw(win)
win.getMouse()
win.close()

"""
def probmatrix(n, p):   #meathod for calculating the initial matrix
    one = 1-p
    z = p
    total = n*n
    z = int(math.floor(total * z))

    one = int(math.ceil(total * one))
    arr = []
    #print(z)
    for i in range(0,z):
        arr.append(0)
    for i in range(0,one):
        arr.append(1)
    if( len(arr) > n*n):
        arr.remove(0)
    np.random.shuffle(arr)
    return arr , one



def changesourcedest(val , n , one): #this meathod is to fix the source and the destination block problem. I am basically changing the
    if(val[0][0] == 0): #the values of the source and the destination if they are blocked. I am keeping the probability same by swiching some other value to 0.
        x = random.randint(1,one)
        nth = 0
        for i in range(0,n):
            a = 0
            for j in range(1,n):
                if(val[i][j] == 1 and (i!=n-1 or j != n-1) and x == nth ):
                    val[i][j] =0; #if the values encountered is one then switch it to zero to keep the probability same.
                    val[0][0]= 1;  # switch the source to one.
                    a = 1
                    break;
                elif(val[i][j] == 1):
                    nth = nth+1
            if(a == 1):
                break;
    if(val[n-1][n-1] == 0):  #this is for the destination value. you are doing the same thing again.
        x = random.randint(1,one-1)
        nth = 0
        for i in range(0,n):
            a = 0
            for j in range(1,n):
                if(val[i][j] == 1 and x == nth):
                    val[i][j] =0;
                    val[n-1][n-1]= 1;
                    a = 1
                    break;
                elif(val[i][j] == 1):
                    nth = nth+1
            if(a == 1):
                break;
    return val
def maze(n, prob):
    val = []
    h = 10
    mat, one = probmatrix(n,prob)
    val = np.array(mat).reshape((n,n))
    #print(val[3][3])
    #print(str(val[0][0]) + " " + str(val[1][1]))
    #if( val[0][0] == 0 or val[n-1][n-1] == 0):
    val = changesourcedest(val, n, one)
    def buildmaze(n):
        win = GraphWin("My maze" , n*h ,n*h)
        arr = []
        l = 0
        k = h
        for i in range(0,n):
            for j in range(0,n):
                shape = Rectangle(Point(l, i*h), Point(k,h*(i+1)))
                #print(l)
                shape.setOutline("blue")
                shape.setFill("white")
                arr.append(shape)
                l = l+h
                k = k+h
            l=0
            k =h
        return win, arr

    w , arr = buildmaze(n)
    w.setBackground('black')
    arr = np.array(arr)
    arr = arr.reshape((n,n))
    #print( arr.shape)
    for i in range(0,n):
        for j in range( 0 , n):
            #print(arr[i][j])
            if( val[i][j] == 0):
                arr[i][j].setFill("black")
                arr[i][j].draw(w)
            else:
                arr[i][j].draw(w)
    #m = np.array((10,10))
    #print(val)
    return w, val, arr
#print(valt)

 #this is for bidirectional BFS
def bidbfs(val , n , arr):
    value1, value2, fringesize, absmax = BidBFS.bidbfs(val, n)
    #print(value1,value2)
    length = 0
    temp = value1
    temp1 = 0
    temp2 = value2
    if(value1 != 0 and value2 !=0):
        while( value1 != None):
            print(str(value1.nodex) + " " + str(value1.nodey) )
            arr[value1.nodex][value1.nodey].setFill("red")
            value1 = value1.prvnode
            length = length +1
        while( value2 != None):
            print(str(value2.nodex) + " " + str(value2.nodey) )
            arr[value2.nodex][value2.nodey].setFill("red")
            temp1= value2
            value2 = value2.prvnode
            length = length +1
        temp1.prvnode = temp
        if(value1 !=None):
            arr[n-1][n-1].setFill("red")
            length = length +1
        return temp2 , fringesize , length , absmax
    return None , fringesize , length , absmax

 #this is for rew.getMouse()gular bfs
def runbfs(val, arr, n):
    length =0
    value , visited, absmax = bfs.bfs(val,n)
    if( value == None):
        print( "no path to be found")
    else:
        temp = value
        while( value.prvnode != None):
            print(str(value.prvnode.nodex) + " " + str(value.prvnode.nodey) )
            arr[value.prvnode.nodex][value.prvnode.nodey].setFill("yellow")
            value = value.prvnode
            length = length+1
    if(value !=None):
        arr[n-1][n-1].setFill("yellow")
        length = length +1
        return temp, visited
    return None , visited


#valt = [[1,0,0,1],[1, 1 ,1,1],[1, 1, 1, 0],[1,1,0,1]]
#print(valt)
def astartalgo(algo, val , n , arr):
    minvisited = n*n
    minvalues = 0
    length=0
    max =0
    absmax =0
    for i in range(0,20):
        value , visited , max = Astar.astarED(val,n,algo)
        if( value == None):
            print( "no path to be found")
        else:
            if( visited.qsize() < minvisited):
                absmax= max
                minvalues = value
                minvisited = visited.qsize()
    print(i)
    temp = minvalues
    if(minvalues != 0):
        while( minvalues.prvnode != None):
            length =length+1
            #print(str(value.prvnode.nodex) + " " + str(value.prvnode.nodey) )
            arr[minvalues.prvnode.nodex][minvalues.prvnode.nodey].setFill("red")
            minvalues = minvalues.prvnode

        if(minvalues != 0):
            arr[n-1][n-1].setFill("red")
            length = length +1
    else:
        return None, minvisited, length, absmax
    return temp, minvisited, length, absmax
def reset(arr, value):
    if(value != None ):
        while( value.prvnode != None):
            #print(str(value.prvnode.nodex) + " " + str(value.prvnode.nodey) )
            arr[value.prvnode.nodex][value.prvnode.nodey].setFill("white")
            value = value.prvnode
        arr[n-1][n-1].setFill("white")
def rundfs(val, n):
    start = dfs.node(0,0)
    #dfs.dfs(start, val,n)
    dfs.dfs(start,val,n)
    for visited in dfs.visited:
        arr[visited[0]][visited[1]].setFill("green")
    #return dfs.visitedlength
n = 10
prob = 0.2
w, val , arr = maze(n, prob)
resetvalues, visited = runbfs(val, arr, n)
w.getMouse()
if( resetvalues != None):
    reset(arr , resetvalues)
resetvaluest ,fringesize , length , absma = bidbfs(val , n , arr)
w.getMouse()
if( resetvalues != None):
    reset(arr , resetvalues)
resetvalues, minvisited, length, absmax = astartalgo(0, val , n , arr) #ED
w.getMouse()
if( resetvalues != None):
    reset(arr , resetvalues)
resetvalues,  minvisited, length, absmax = astartalgo(1,val , n , arr) #MH Distance

w.getMouse()

"""
with open('maxfringe-40astar1.csv', 'wb') as csvfile:#, open('fringe-40bfs.csv', 'wb') as b:
    for i in range(1,50):
        i = float(i)
        prob = i/100
        #print(prob)
        n = 50
        w, val , arr = maze(n, prob)
        #rundfs(val, n)
        a, b ,c , absmax = astartalgo(1, val , n , arr)
        #dfs.visited = []
        #dfs.stack = []

        #w.getMouse()
        #v = 0
        #for q_item in visited.queue:
        #    v = v +1
        #if(resetvalues != None):

            #reset(arr , resetvalues)

        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([str(prob), absmax])
        #dfs.lengthvisited= []
            #filewriter1 = b.writer(b, delimiter=',',
                                        #quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #filewriter1.writerow([str(prob), visited.qsize()])
        #else:
            #print("NP")

            #filewriter = csv.writer(csvfile, delimiter=',',
                                        #quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #filewriter.writerow([str(prob), v])
            #filewriter1 = b.writer(b, delimiter=',',
                                        #quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #filewriter1.writerow([str(prob), visited.qsize()])
#print(value)
#print("outside")
"""
#w.getMouse()
#w.close()
