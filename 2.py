from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

window_size = 300
FPS = 60
x = 0
angle = 320
mode = 1

def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)

def draw():
	global x
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,0,0)
	glVertex2f(x+0,85)
	for i in range(0,361,1):
		glVertex2f(x+15*math.cos(math.radians(i)),15*math.sin(math.radians(i))+85)
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,0,0)
	glVertex2f(x+0,45)
	for i in range(0,361,1):
		glVertex2f(x+25*math.cos(math.radians(i)),25*math.sin(math.radians(i))+45)
	glEnd()
	
	glBegin(GL_POLYGON)
	glColor3f(1,1,1)
	glVertex2f(x+-80,25)
	glVertex2f(x+-50,0)
	glVertex2f(x+50,0)
	glVertex2f(x+80,25)
	glEnd()
	
	glBegin(GL_POLYGON)
	glColor3f(0,0,1)
	glVertex2f(-300,0)
	glVertex2f(300,-0)
	glVertex2f(300,-300)
	glVertex2f(-300,-300)
	glEnd()	
	
	
	
	glBegin(GL_LINES)
	glColor3f(0,0,0)
	glVertex2f(x+0,50)
	glVertex2f(x+30*math.cos(math.radians(angle)),0*math.sin(math.radians(angle)))
	glEnd()
	
	glFlush()
def animate(value):
	global x,angle,mode
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,0)
	if(x<window_size):
		x+=1
	else:
		x=-window_size
	if(mode==1):
		if(angle>=230):
			angle-=1
		else:
			mode = 0
	else:
		if(angle<=320):
			angle+=1
		else:
			mode = 1
def main():
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutCreateWindow("Boat")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	Init()
	glutMainLoop()
main()
