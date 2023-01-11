from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE=1000

def plot_points(x,y):
	glClear(GL_COLOR_BUFFER_BIT)
	glPointSize(3.0)
	glColor3f(0.6,0.4,0.2)
	glBegin(GL_TRIANGLES)
	glVertex2f(0.5+x,0+y)
	glVertex2f(-0.5+x,0+y)
	glVertex2f(0+x,0.5+y)
	glEnd()
		
	glFlush()	

def main():
	x = float(input("Enter offset of x coordinate :"))
	y = float(input("Enter offset of y coordinate :"))
	glutInit()
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutCreateWindow("Test!")
	glutDisplayFunc(lambda: plot_points(x,y))
	glutMainLoop()
	
main()	
