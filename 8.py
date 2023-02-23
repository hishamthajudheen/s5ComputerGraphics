from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

window_size=500
angle = 0
FPS = 60
x = 0

def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)
def draw():
	global angle,x
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	glColor3f(1,0,0)
	glVertex2f(x+-100,0)
	glVertex2f(x+-100,50)
	glVertex2f(x+-60,50)
	glVertex2f(x+-60,100)
	glVertex2f(x+60,100)
	glVertex2f(x+60,50)
	glVertex2f(x+100,50)
	glVertex2f(x+100,0)
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,1,1)
	glVertex2f(x+-50,0)
	for i in range(0,361,1):
		glVertex2f(x+25*math.cos(math.radians(i))-50,25*math.sin(math.radians(i)))
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,1,1)
	glVertex2f(x+50,0)
	for i in range(0,361,1):
		glVertex2f(x+25*math.cos(math.radians(i))+50,25*math.sin(math.radians(i)))
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,0)
	glVertex2f(x+-50,0)
	glVertex2f(x+25*math.cos(math.radians(angle))-50,25*math.sin(math.radians(angle)))
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,0)
	glVertex2f(x+50,0)
	glVertex2f(x+25*math.cos(math.radians(angle))+50,25*math.sin(math.radians(angle)))
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0.5,0.3,0)
	glVertex2f(-500,-25)
	glVertex2f(500,-25)
	glEnd()
	
	glFlush()
	
def animate(value):
	global angle,x
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,0)
	if(x<window_size):
		x+=5
		angle-=2
	else:
		x=-window_size
		angle=0

def main():
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutCreateWindow("car")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	Init()
	glutMainLoop()
main()
