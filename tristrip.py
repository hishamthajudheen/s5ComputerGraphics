import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
def plot_points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glPointSize(5.0)
    glBegin(GL_LINE_STRIP)       
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5) 
    glVertex2f(1.0,0.5)
    glVertex2f(0.5, -0.5)  
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.0, 0.5) 
    glEnd()       
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Triangle Strip!")
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot_points)
clearScreen()
glutMainLoop()
