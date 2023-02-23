from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import random

window_size = 500
mode = 1
FPS = 60
angle1 = 225 
angle2 = 315
ry  = 470
mx = 0

def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)
def draw():
	global angle1,angle2,ry,rx
	glClear(GL_COLOR_BUFFER_BIT)
	
	glPointSize(3)
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(-470,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(-400,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(-370,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(200,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(0,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(150,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(-70,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(450,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(480,ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(200,-50+ry)
	glEnd()
	glBegin(GL_POINTS)
	glColor3f(0,0,1)
	glVertex2f(200,-80+ry)
	glEnd()
	
	glBegin(GL_LINES) #body
	glColor3f(1,0,0)
	glVertex2f(mx+0,100)
	glVertex2f(mx+0,-100)
	glEnd()
	
	glBegin(GL_LINES) #arms
	glColor3f(1,0,0)
	glVertex2f(mx+50,30)
	glVertex2f(mx+-50,30)
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN) #head
	glColor3f(1,0,0)
	glVertex2f(mx+0,130)
	for i in range(0,361,1):
		glVertex2f(mx+30*math.cos(math.radians(i)),30*math.sin(math.radians(i))+100)
	glEnd()
	
	glBegin(GL_LINES)	#rightleg
	glColor3f(1,0,0)
	glVertex2f(mx+0,-100)
	glVertex2f(mx+40+30*math.cos(math.radians(angle2)),-160+30*math.cos(math.radians(angle2)))
	glEnd()
	
	glBegin(GL_LINES)	#leftleg
	glColor3f(1,0,0)
	glVertex2f(mx+0,-100)
	glVertex2f(mx+-40+30*math.cos(math.radians(angle1)),-160+30*math.cos(math.radians(angle1)))
	glEnd()
	
	glBegin(GL_LINES)	#kodakkambi
	glColor3f(0,1,0)
	glVertex2f(mx+50,30)
	glVertex2f(mx+50,200)
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN) #Umbrella
	glColor3f(1,0,0)
	glVertex2f(mx+50,200)
	for i in range(0,181,1):
		glVertex2f(mx+60*math.cos(math.radians(i))+50,60*math.sin(math.radians(i))+200)
	glEnd()
	
	glLineWidth(4)
	glBegin(GL_LINES)
				#ground
	glColor3f(1,1,0)
	glVertex2f(-500,-160)
	glVertex2f(500,-160)
	glEnd()
	
	
		
	glFlush()
	
def animate(value):
	global mode,angle1,angle2,ry,rx,mx
	if(mx<500):
		mx += 1
	else:
		mx = -500
	if(mode == 1):
		if(angle1<315 and angle2>225):
			angle1+=1
			angle2-=1
			if(ry>-160):
				ry-=1		
			else:
				ry = 470
			
		else:
			mode = 0
	if(mode == 0):
		if(angle1>=225 and angle2<315):
			angle1-=1
			angle2+=1
			if(ry>-160):
				ry-=1
			else:
				ry = 470
		else:
			mode = 1
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,int(0))
def main():
	glutInit()
	glutCreateWindow("Blah")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	Init()
	glutMainLoop()
main()
