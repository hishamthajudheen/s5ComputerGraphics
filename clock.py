from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

window_size=500
angleh = 90
anglem = 90
angles = 90 
FPS = 900

def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)

def draw():
	global angles,anglem,angleh
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,1,1)
	glVertex2f(0,0)
	for i in range(0,361,1):
		glVertex2f(200*math.cos(math.radians(i)),200*math.sin(math.radians(i)))	
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,0)
	glVertex2f(0,0)
	glVertex2f(100*math.cos(math.radians(angleh)),100*math.sin(math.radians(angleh)))
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,1)
	glVertex2f(0,0)
	glVertex2f(150*math.cos(math.radians(anglem)),150*math.sin(math.radians(anglem)))
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(1,0,0)
	glVertex2f(0,0)
	glVertex2f(180*math.cos(math.radians(angles)),180*math.sin(math.radians(angles)))
	glEnd()
	
	glFlush()
def animate(value):
	global angles,anglem,angleh
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,0)
	angles-=1
	anglem-=1/60
	angleh-=(1/3600)*6
	
def main():
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutCreateWindow("clock")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	Init()
	glutMainLoop()
main()
