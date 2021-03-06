# Joseph Rice 12/17/2017
from visual import*
from math import *
scene.width = 1000
scene.height = 1000
scene.title = "Vectors"

##xaxis = cylinder(pos=(-10,0,0),axis=(20,0,0),radius=0.2,color=color.yellow)
##yaxis = cylinder(pos=(0,-10,0),axis=(0,20,0),radius=0.2,color=color.yellow)
print("The cube will slowly grow and shrink over time")
class vector:
    def __init__ (self,x,y,z,ax=0,ay=0,az=0):
        """X,Y,Z tell pos of base"""
        # tells axis pos ax,ay,az,
        self.x = x
        self.y = y
        self.z = z
        self.ax = ax
        self.ay = ay
        self.az = az
        self.Vector = arrow(pos=(self.x,self.y,self.z),axis=(self.ax,self.ay,self.az),\
        shaftwidth=.18,headwidth=.3,headlength=.4,color=color.cyan,material=materials.blazed)
    def length(self):
        value = float(self.Vector.shaftwidth/0.09)
        return value
    def vector_grow_x(self,incriment):
        self.Vector.axis.x += incriment
    def vector_shrink_x(self,incriment):
        self.Vector.axis.x -= incriment
    def vector_grow_y(self,incriment):
        self.Vector.axis.y += incriment
    def vector_shrink_y(self,incriment):
        self.Vector.axis.y -= incriment
    def vector_grow_z(self,incriment):
        self.Vector.axis.z += incriment
    def vector_shrink_z(self,incriment):
        self.Vector.axis.z -= incriment
    def x_axis(self):
        return self.Vector.axis.x

def grow_box(box,rate):
    box.length +=rate
    box.width +=rate
    box.height += rate

def shrink_box(box,rate):
    if box.length >=0:
        box.length -=rate
        box.width -= rate
        box.height -= rate
    else:
        box.length += rate
        box.width += rate
        box.height += rate



Center_ball = sphere(pos=(0,0,-1),radius=0.2,color=color.cyan,\
material=materials.blazed)

v = vector(0,float(Center_ball.radius),cos(pi),0,1,0)
v2 = vector(float(Center_ball.radius),0,cos(pi),1,0,0)
v3 = vector(float(cos(pi)*Center_ball.radius),0,cos(pi),cos(pi),sin(pi),0)
v4 = vector(0,float(cos(pi)*Center_ball.radius),cos(pi),0,sin(radians(270)),0)
v5 = vector(0,0,float(Center_ball.radius-1),0,0,1)
v6 = vector(0,0,float(cos(pi)*Center_ball.radius-1),0,0,sin(radians(270)))
Box = box(pos=(0,0,-1),length=2*Center_ball.radius+v.length(),\
width=2*Center_ball.radius+v.length(),\
height=2*Center_ball.radius+v.length(),color=color.yellow,opacity=0.2)

n = 500
n2 = 1000
n3 = 800
n4 = 100
# you can change this to make it faster or slower
multiply = 0.5

while True:
    n += 10
    n2 +=10
    n3 +=10
    n4 += 10
    for i  in range(1,500):
        rate(multiply*1000)
        v.vector_grow_y(0.01)
        v2.vector_grow_x(0.01)
        v3.vector_shrink_x(0.01)
        v4.vector_shrink_y(0.01)
        v5.vector_grow_z(0.01)
        v6.vector_shrink_z(0.01)
        grow_box(Box,0.02)

    for i in range(1,500):

        rate(multiply*1000)
        v.vector_shrink_y(0.01)
        v2.vector_shrink_x(0.01)
        v3.vector_grow_x(0.01)
        v4.vector_grow_y(0.01)
        v5.vector_shrink_z(0.01)
        v6.vector_grow_z(0.01)
        shrink_box(Box,0.02)

    for i in range(1,n2):
        rate(multiply*1000)
        v.vector_grow_y(0.01)
        v2.vector_grow_x(0.01)
        v3.vector_shrink_x(0.01)
        v4.vector_shrink_y(0.01)
        v5.vector_grow_z(0.01)
        v6.vector_shrink_z(0.01)
        grow_box(Box,0.02)
        try:
            for i in range(1,n3):
                rate(multiply*1000)
                v.vector_shrink_y(0.01)
                v2.vector_shrink_x(0.01)
                v3.vector_grow_x(0.01)
                v4.vector_grow_y(0.01)
                v5.vector_shrink_z(0.01)
                v6.vector_grow_z(0.01)
                shrink_box(Box,0.02)
        except:

          for i in range(1,500):
              rate(multiply*1000)
              v.vector_grow_y(0.01)
              v2.vector_grow_x(0.01)
              v3.vector_shrink_x(0.01)
              v4.vector_shrink_y(0.01)
              v5.vector_grow_z(0.01)
              v6.vector_shrink_z(0.01)
              grow_box(Box,0.02)

        try:
            for i in range(1,n4):
                rate(multiply*900)
                v.vector_shrink_y(0.01)
                v2.vector_shrink_x(0.01)
                v3.vector_grow_x(0.01)
                v4.vector_grow_y(0.01)
                v5.vector_shrink_z(0.01)
                v6.vector_grow_z(0.01)
                shrink_box(Box,0.02)
        except:
            for i in range(1,500):
              rate(multiply*1000)
              v.vector_grow_y(0.01)
              v2.vector_grow_x(0.01)
              v3.vector_shrink_x(0.01)
              v4.vector_shrink_y(0.01)
              v5.vector_grow_z(0.01)
              v6.vector_shrink_z(0.01)
              grow_box(Box,0.02)
