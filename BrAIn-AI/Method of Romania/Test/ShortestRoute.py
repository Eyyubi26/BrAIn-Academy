#WARNING! This code is a sample code that shows how the "Method of Romania" works.
import tkinter as tk
from tkinter import *
import time
import queue
import os
import sys

#Create Grid
def create_grid(event=None):
    w = Frame.winfo_width() # Get current width of canvas
    h = Frame.winfo_height() # Get current height of canvas
    Frame.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, N):
        Frame.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, N):
        Frame.create_line([(0, i), (w, i)], tag='grid_line')
#Create Shape
def CreateShape(x,y,Time,color):
	time.sleep(Time)
	distx = N*x;disty = N*y
	Frame.create_rectangle(5+distx, 5+disty, N-5 +distx, N-5 +disty, outline='white', fill=color)
	Frame.update()
#Event Origin
def dragOrigin(eventorigin):
      x = eventorigin.x
      y = eventorigin.y
      x = int(x/N)
      y = int(y/N)
      if(x == Start[0] and y == Start[1]):
      	return 0
      elif(x == End[0] and y == End[1]):
      	return 0
      else:
      	Block[x][y] = 1
      	CreateShape(x,y,0,"pink")
#startBFS
def getorigin(eventorigin):
	x = eventorigin.x
	y = eventorigin.y
	x = int(x/N)
	y = int(y/N)
	if(Start[0]!= -1):
		if(End[0]!=-1):
			if(x == Start[0] and y == Start[1]):
				CreateShape(Start[0],Start[1],0,"white")
				Start[0] = -1
				Start[1] = -1
			elif(x == End[0] and y == End[1]):
				CreateShape(End[0],End[1],0,"white")
				End[0] = -1
				End[1] = -1
		elif(x != Start[0] or y != Start[1]):
			End[0] = x
			End[1] = y
			CreateShape(x,y,0,"Orange")
	elif(x != End[0] or y != End[1]):
		Start[0] = x
		Start[1] = y
		CreateShape(x,y,0,"Red")	
#Restart
def restart_program():
    python = sys.executable
    clear = lambda: os.system('cls')
    clear()
    os.execl(python, python, * sys.argv)
def Run_BFS_search():
	flag = BFS()
	print(flag)
	if(flag == True):
		traceBack()
#Init Grid
def InitMatrix():
	#Start log
	print("İşleniyor...")
	#Gobal varaiable
	global Frame,N,root,Start,End,sizeX,sizeY,Block
	root = tk.Tk()
	sizeX = 50
	sizeY = 50
	Block = [ [0 for i in range(sizeX+10)] for i in range(sizeY+10)]
	N = 30
	#Title
	root.title("Method of Romania by BrAIn-AI")
	#Button
	frame = Frame(root)
	frame.pack()
	Restart_button = Button(frame, text="Restart", command=restart_program,
		bg = "yellow",activebackground="green2",activeforeground="black").pack(side = LEFT)
	Run_Button = Button(frame, text="Searching", command=Run_BFS_search,
		bg = "green2",activebackground="yellow",activeforeground="blue").pack(side = LEFT)
	#Frame
	Frame = tk.Canvas(root, height=1500, width=1500, bg='white')
	Frame.pack(fill=tk.BOTH, expand=True)
	Frame.bind('<Configure>', create_grid)
	# Frame.bind("<Button 1>",getorigin)
	Frame.bind("<Button 1>",getorigin)
	Frame.bind("<B1-Motion>",dragOrigin)
	#Start Cell: color Red
	Start = ([5,6])
	CreateShape(Start[0],Start[1],0,"Red")
	#End Cell: color Orange
	End = ([30,20])
	CreateShape(End[0],End[1],0,"Orange")
#printTrackback
#printTrack
def traceBack():
	x = End[0]
	y = End[1]
	a = path[x][y][0]
	b = path[x][y][1]
	while(a!=-1 and b!=-1):
		if(x != End[0] or y != End[1]):
			CreateShape(x,y,0,"magenta")
		x = a
		y = b
		a = path[x][y][0]
		b = path[x][y][1]

#BFS
def BFS():
	BaseTime = 0
	global path,dist
	path = [[([]) for i in range(sizeX+10)] for i in range(sizeY+10)]
	dist = [[0 for i in range(sizeX+10)] for i in range(sizeY+10)]
	#direct up, right, down, left
	dx = [0,1,0,-1]
	dy = [-1,0,1,0]
	#Used init 2d array all zero
	used = [[0 for i in range(sizeX+10)] for i in range(sizeY+10)]
	#Queue
	q = queue.Queue(maxsize = sizeX*sizeY+10)
	path[Start[0]][Start[1]] = ([-1,-1])
	q.put([Start[0],Start[1]])
	while(q.empty() == False):
		Front = q.get()
		#Avoid going to used vertice
		if(used[Front[0]][Front[1]] == 1):
			continue
		#Process end when vertice go to End point
		if(Front[0] == End[0] and Front[1] == End[1]):
			CreateShape(Start[0],Start[1],BaseTime,"Red")
			CreateShape(End[0],End[1],BaseTime,"Green2")
			return True
		if(Front != Start):
			CreateShape(Front[0],Front[1],BaseTime,"yellow")
			CreateShape(Front[0],Front[1],BaseTime,"blue")
		#Mark this vertice used
		used[Front[0]][Front[1]] = 1
		for i in range(4):
			X = Front[0]+dx[i]
			Y = Front[1]+dy[i]
			if(used[X][Y] == 1):
				continue
			if(Block[X][Y] == 0):
				if(X>=0 and X <= sizeX and Y>=0 and Y<=sizeY):
					#print('Co',X,Y,used[X][Y])
					#CreateShape(X,Y,"blue")
					dist[X][Y] = dist[Front[0]][Front[1]]+1
					path[X][Y] = ([Front[0],Front[1]])
					q.put([X,Y])
	return False		
#Main
InitMatrix()
#loop
root.mainloop()
