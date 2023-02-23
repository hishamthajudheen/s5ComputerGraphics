from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

window_size=500
FPS = 60
angle = 0
angle2 = 90
def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)
	
def draw():
	global angle,angle2
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,1,0)
	glVertex2f(0,0)
	for i in range(0,361,1):
		glVertex2f(50*math.cos(math.radians(i)),50*math.sin(math.radians(i)))
	glEnd()
	
	glBegin(GL_POINTS)
	glColor3f(1,1,1)
	for i in range(0,361,6):
		glVertex2f(300*math.cos(math.radians(i)),200*math.sin(math.radians(i)))
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(0.5,0.6,0.4)
	glVertex2f(300*math.cos(math.radians(angle)),200*math.sin(math.radians(angle)))
	for i in range(0,361,1):
		glVertex2f(300*math.cos(math.radians(angle))+(25*math.cos(math.radians(i))),200*math.sin(math.radians(angle))+(25*math.sin(math.radians(i))))
	glEnd()
	
	glBegin(GL_POINTS)
	glColor3f(1,1,1)
	for i in range(0,361,4):
		glVertex2f(400*math.cos(math.radians(i)),300*math.sin(math.radians(i)))
	glEnd()
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(0.2,0.9,0.8)
	glVertex2f(400*math.cos(math.radians(angle2)),300*math.sin(math.radians(angle2)))
	for i in range(0,361,1):
		glVertex2f(400*math.cos(math.radians(angle2))+(30*math.cos(math.radians(i))),300*math.sin(math.radians(angle2))+(30*math.sin(math.radians(i))))
	glEnd()
	
	glFlush()

def animate(value):
	global angle,angle2
	glutPostRedisplay()
	glutTimerFunc(int(FPS/1000),animate,0)
	time.sleep(0.01)
	angle+=1
	angle2-=1

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
