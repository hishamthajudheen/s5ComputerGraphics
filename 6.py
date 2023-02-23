from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

window_size = 500
FPS = 5
y = 0
ky = 0

def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)
	
def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glLineWidth(5)
	glBegin(GL_LINES)
	glColor3f(0,1,0)
	glVertex2f(-200,200)
	glVertex2f(-200,0)
	glEnd()	
	glBegin(GL_LINES)
	glColor3f(0,1,0)
	glVertex2f(-200,0)
	glVertex2f(200,0)
	glEnd()	
	glBegin(GL_LINES)
	glColor3f(0,1,0)
	glVertex2f(200,0)
	glVertex2f(200,200)
	glEnd()
	
	glBegin(GL_POLYGON)
	glColor3f(0,0,1)
	glVertex2f(-200,0)
	glVertex2f(200,0)
	glVertex2f(200,y+50)
	glVertex2f(-200,y+50)
	glEnd()
	
	glBegin(GL_POLYGON)
	glColor3f(0.5,0.3,0)
	glVertex2f(-200,0)
	glVertex2f(200,0)
	glVertex2f(200,ky)
	glVertex2f(-200,ky)
	glEnd()

		
	
	glFlush()

def animate(value):
	global y,ky
	glutPostRedisplay()
	glutTimerFunc(int(FPS/1000),animate,0)
	if(y<150):
		time.sleep(0.03)
		y+=0.5
		ky+=0.5
	else:
		y=0
		ky=0

def main():
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutCreateWindow("bucket")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	Init()
	glutMainLoop()
main()
