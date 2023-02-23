from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

window_size = 600
FPS = 60
angle1 = 180
angle2 = 360

def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)

def draw():
	global x
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	glColor3f(1,0,0)
	glVertex2f(0,250)
	glVertex2f(-120,0)
	glVertex2f(120,0)
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(1,1,1)
	glVertex2f(0,250)
	glVertext2f(0,350)
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(1,1,1)
	glVertex2f(0,250)
	glVertext2f(0,350)
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,1,1)
	glVertex2f(0,250)
	for i in range(0,361,1):
		glVertex2f(-20*math.cos(math.radians(i)),20*math.sin(math.radians(i))+250)
	glEnd()
	
	glFlush()
def animate(value):
	global angle
	glutPostRedisplay()
	glutTimerFunc(int(1000)/FPS,animate,0)	
	angle1+=1
	angle2-=1
def main():
	glutInit()
	glutCreateWindow("WindMill")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	Init()
	glutMainLoop()
main()
