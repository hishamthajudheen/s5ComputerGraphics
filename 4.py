from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

window_size = 300
FPS = 60
angle1= 0
angle2=180
mode = 1

def Init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-window_size,window_size,-window_size,window_size)

def draw():
	global angle1,angle2
	glClear(GL_COLOR_BUFFER_BIT)
	
	
	glBegin(GL_POLYGON)
	glColor3f(1,0,0)
	glVertex2f(0,0)
	glVertex2f(-120,-100)
	glVertex2f(120,-100)
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,1)
	glVertex2f(0,0)
	glVertex2f(250*math.cos(math.radians(angle1)),250*math.sin(math.radians(angle1)))
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(0,0,1)
	glVertex2f(0,0)
	glVertex2f(250*math.cos(math.radians(angle2)),250*math.sin(math.radians(angle2)))
	glEnd()
	
	glFlush()
def animate(value):
	global angle2,angle1,mode
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,0)

	if(mode==1):
		if(angle2 <210 and angle1 <30):
			angle2 +=1
			angle1 +=1
		else:
			mode = 0
	if(mode==0):
		if(angle2>150 and angle1>-30):
			angle2 -=1
			angle1 -=1
		else:
			mode = 1
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
