from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOW_SIZE = 500
SCALE = 100
xc = yc = 0
r = 1
def init_display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 1, 0)
	glPointSize(2)
def midpoint_circle():
	glBegin(GL_POINTS)
	global xc, yc, r
	x, y = 0, r
	p = 1 - r
	plot_symmetric_points(x, y)
	while x < y:
		x += 1
		if p < 0:
			p += 2 * x + 1
		else:
			y -= 1
			p += 2 * (x - y) + 1
		plot_symmetric_points(x, y)
	glEnd()
	glFlush()

def plot_symmetric_points(x, y):
	global xc, yc
	glVertex2f((xc + x) / SCALE, (yc + y) / SCALE)
	glVertex2f((xc + x) / SCALE, (yc - y) / SCALE)
	glVertex2f((xc - x) / SCALE, (yc + y) / SCALE)
	glVertex2f((xc - x) / SCALE, (yc - y) / SCALE)
	glVertex2f((xc + y) / SCALE, (yc + x) / SCALE)
	glVertex2f((xc + y) / SCALE, (yc - x) / SCALE)
	glVertex2f((xc - y) / SCALE, (yc + x) / SCALE)
	glVertex2f((xc - y) / SCALE, (yc - x) / SCALE)
def no_circle():
	pass
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
	glutInitWindowPosition(50, 50)
	global xc, yc, r
	xc = int(input("Enter x coordinate of the centre "))
	yc = int(input("Enter y coordinate of the centre "))
	r = float(input("Enter length of radius "))
	glutCreateWindow("Circle using Midpoint")
	init_display()
	glutDisplayFunc(midpoint_circle)
	glutMainLoop()
main()
