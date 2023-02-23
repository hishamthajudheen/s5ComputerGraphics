from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

window_size = 500
FPS = 60
mode = 1
x=y=0
def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,0,0)
	glVertex(x+0,y+0)
	for i in range(0,361,1):
		glVertex2f(x+30*math.cos(math.radians(i)),y+30*math.sin(math.radians(i)))
	glEnd()
	
	glLineWidth(3)
	glBegin(GL_LINES)
	glColor3f(1,1,1)
	glVertex(-window_size,-33)
	glVertex(window_size,-33)
	glEnd()
	
	glFlush()
def animate(temp):
	global x,y,mode
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,0)
	if(mode == 1):
		if(y<150):
			x+=0.3
			y+=0.4
		else:
			mode=0
	else:
		if(y>0):
			x+=0.3
			y-=0.4
		else:
			mode=1
		
def main():
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutCreateWindow("ball")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	Init()
	glutMainLoop()
main()
