from graphics import *
import numpy as np
import math
import random
import bfs
import test
"""
def strategy1(val,arr,n ):
    a,b = test.runbfs(val,arr,n)
    x = []
    while(a!= None):
        x.append((a.nodex,a.nodey))
        a = a.prvnode
    return x
"""
def coloring(arr,maze,n): #colring the new maze red based on the fire spreading
    for i in range (0,n):
        for j in range(0,n):
            if maze[i][j] == 2:
                arr[i][j].setFill("red")

def probmatrix(n, p):   #meathod for calculating the initial matrix
    one = 1-p
    z = p
    total = n*n
    z = int(math.floor(total * z))

    one = int(math.ceil(total * one))
    arr = []
    #print(z)
    for i in range(0,z-1): #So i made it z-1 so there will be one free block
        arr.append(0)
    arr.append(2) #then I appended a value 2 so when it randomly shuffles, one of the blocks will be on fire
    for i in range(0,one):
        arr.append(1)

    np.random.shuffle(arr)
    return arr
n = 15

def changesourcedest(arr , n): #this meathod is to fix the source and the destination block problem. I am basically changing the
    if(val[0][0] == 0): #the values of the source and the destination if they are blocked. I am keeping the probability same by swiching some other value to 0.
        for i in range(0,n):
            a = 0
            for j in range(1,n):
                if(val[i][j] == 1 and (i!=n-1 or j != n-1) ):
                    val[i][j] =0; #if the values encountered is one then switch it to zero to keep the probability same.
                    val[0][0]= 1;  # switch the source to one.
                    a = 1
                    break;
            if(a == 1):
                break;
    if(val[n-1][n-1] == 0):  #this is for the destination value. you are doing the same thing again.
        for i in range(0,n):
            a = 0
            for j in range(1,n):
                if(val[i][j] == 1):
                    val[i][j] =0;
                    val[n-1][n-1]= 1;
                    a = 1
                    break;
            if(a == 1):
                break;
    return arr

val = np.array(probmatrix(n,0.2)).reshape((n,n))
print(val)
if( val[0][0] == 0 or val[n-1][n-1] == 0):
    val = changesourcedest(val, n)

def buildmaze(n):
    win = GraphWin("My maze" , n*40 ,n*40)
    arr = []
    l = 0
    k = 40
    for i in range(0,n):
        for j in range(0,n):
            shape = Rectangle(Point(l, i*40), Point(k,40*(i+1)))
            #print(l)
            shape.setOutline("blue")
            shape.setFill("white")
            arr.append(shape)
            l = l+40
            k = k+40
        l=0
        k =40
    return win, arr

w , arr = buildmaze(n)
w.setBackground('black')
arr = np.array(arr)
arr = arr.reshape((n,n))
print( arr.shape)

for i in range(0,n): #initial drawing based on val maze
    for j in range(0 , n):
        #print(arr[i][j])
        if( val[i][j] == 0):
            arr[i][j].setFill("black")
            arr[i][j].draw(w)
        elif(val[i][j] == 2):
            arr[i][j].setFill("red")
            arr[i][j].draw(w)
        else:
            arr[i][j].draw(w)


#path = strategy1(val,arr,n)

k = 0
random_q_vals = np.full((n, n), 0.5) #makes another matrix of (nxn) of random q values
print(random_q_vals)
def testfn(val,x,y,k): #function to count the number of neighbors that are on fire
    if(x > 0 and val[x-1][y] == 2):
        k += 1
    if(x < n-1 and val[x+1][y] == 2):
        k += 1
    if(y > 0 and val[x][y-1] == 2 ):
        k += 1
    if(y < n-1 and val[x][y+1] == 2):
        k += 1
    formula = 1 - (1-random_q_vals[x][y])**k #use the formula with q values
    formula = int(random.random()<formula)
    #print(formula)
    if (formula == 1):
        return True
    else:
        return False

for i in range(0,20): #making the two timelines of the mazes
    newMaze = np.zeros([n,n])
    w.getMouse()
    for i in range(0,n):
        for j in range(0,n):
            T = testfn(val,i,j,k)
            if(T == True and val[i][j] != 0):
                newMaze[i][j] = 2
            else:
                newMaze[i][j] = val[i][j]
    coloring(arr,newMaze,n) #calling the coloring function
    val = newMaze
    #print (path)
"""
    for p in path:
        x= p[0]
        y = p[1]
        for i in range(0,n):
            for j in range(0,n):
                if(val[i][j] == 2 and (x == i and y == j)):
                    print("you are burned")
                    w.close()

"""
w.getMouse()
w.close()
