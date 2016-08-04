# encoding: utf-8
"""

@author Yuriseus
@create 2016-6-23 16:32
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

winid=0
WIN_X=500
WIN_Y=500

def init():
    glClearColor(0.0,0.0,0.0,0.0)   #设置背景(清除时的)颜色

def display():
    glClear(GL_COLOR_BUFFER_BIT)    #清除颜色缓冲区 -> 清屏
    glBegin(GL_TRIANGLES)           #绘制三角形，从Begin开始
    glColor3f(1.0,0.0,0.0)          #定义颜色,三个参数分别代表R,G,B成分
    glVertex2f(0.0,1.0)             #顶点坐标(默认的窗口坐标范围是(-1,-1)到(1,1))

    glColor3f(0.0,1.0,0.0)          #绿色
    glVertex2f(-1.0,-1.0)

    glColor3f(0.0,0.0,1.0)          #蓝色
    glVertex2f(1.0,-1.0)
    glEnd();
    glFlush()

def hitkey(key,mousex,mousey):
    global winid
    if (key==b'q'):
        print("Quit")
        glutDestroyWindow(winid)
        sys.exit()

def main():
    global WIN_X,WIN_Y,winid
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)    #单缓冲，RGBA着色方式
    glutInitWindowSize(WIN_X,WIN_Y)
    glutInitWindowPosition(100,100)
    winid=glutCreateWindow("test".encode("cp932"))
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(hitkey)
    glutMainLoop()

if __name__=="__main__":
    main()