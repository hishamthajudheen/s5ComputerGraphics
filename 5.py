from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

window_size = 300
FPS = 120
angle1= 0
angle2=120
angle3=240

def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)

def draw():
	global angle1,angle2
	glClear(GL_COLOR_BUFFER_BIT)
	glLineWidth(10)	
	
	glBegin(GL_POLYGON)
	glColor3f(.9,.5,.3)
	glVertex2f(-5,0)
	glVertex2f(5,0)
	glVertex2f(50,-290)
	glVertex2f(-50,-290)
	
	
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,1)
	glVertex2f(0,0)
	glVertex2f(150*math.cos(math.radians(angle1)),150*math.sin(math.radians(angle1)))
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,1)
	glVertex2f(0,0)
	glVertex2f(150*math.cos(math.radians(angle2)),150*math.sin(math.radians(angle2)))
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,1)
	glVertex2f(0,0)
	glVertex2f(150*math.cos(math.radians(angle3)),150*math.sin(math.radians(angle3)))
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1,0,0)
	glVertex2f(0,0)
	for i in range(0,361,1):
		glVertex2f(20*math.cos(math.radians(i)),20*math.sin(math.radians(i)))
	glEnd()
	
	glFlush()
def animate(value):
	global angle2,angle1,angle3
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,0)

	angle1 +=1
	angle2 +=1
	angle3 +=1
	
	
def main():
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutCreateWindow("seesaw")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	Init()
	glutMainLoop()
main()
