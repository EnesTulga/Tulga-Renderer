# Coded by Enes Tulga
# You can test the code with your own OBJ Files. But I do not guarantee for the best performance.

# IMPORTING GL LIBRARIES

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# -------------------------

# Reading OBJ files
dosya = open("ObjFiles/Centaur.obj", "r")	# Give the first parameter as obj file directory.
model = dosya.read()
# ------------------------------

noktalar = []   # Verticies
yuzler = []	# Faces

#  The Function that finds verticies in model variable (obj file) and assign to noktalar array
def noktaBulucu():
	global model
	global noktalar
	i = 0
	gecici = ""
	flag = False
	while(i < len(model)):
		if(flag):
			flag = False
			if(model[i] == 'v' and model[i + 1] == " "):
				i += 1
				
				while(model[i] != "\n"):
					if(model[i] != " "):
						gecici += model[i]
						i += 1
						if(model[i] == " " or model[i] == "\n"):
							
							noktalar.append(float(gecici))
							gecici = ""
							
					else:
						i += 1
				continue			
		if(model[i] == "\n"):
			flag = True
		i += 1

#  The Function that finds faces in model variable (obj file) and assign to yuzler array
def yuzBulucu():
	global model
	global yuzler
	i = 0
	gecici = ""
	geciciDizi = []
	flag = False
	while(i < len(model)):
		if(flag):
			flag = False
			if(model[i] == 'f' and model[i + 1] == " "):
				
				i += 1
				
				while(model[i] != "\n"):
					if(model[i] != " "):
						gecici += model[i]
						i += 1
						
						if(model[i] == "/"):
							geciciDizi.append(int(gecici) - 1)
							gecici = ""
							while(model[i] != " " and model[i] != "\n"):
								i += 1
						if(model[i] == "\n" or model[i + 1] == "\n"):
							
							yuzler.append(geciciDizi)
							geciciDizi = []
					else:
						i += 1				
		if(model[i] == "\n"):
			flag = True
		i += 1


# This function drawing 3D model in yuzler and noktalar arrays in angle depends on a and b parameter.
#	a = {0 : X, 1: Y, 2: Z}
#	b = {0 : X, 1: Y, 2: Z}
#    Also, x and y parameter defines that where is the starting of the frame. 
def vektorelCizdir(a,b, x, y):
	for yuz in yuzler:
		glBegin(GL_POLYGON)
		for nokta in yuz:
			glVertex2f(noktalar[nokta*3 + a] + x, noktalar[nokta*3 + b] + y)
		glEnd()
noktaBulucu()
yuzBulucu()

# JUST MODEL SCALING

sag = noktalar[0]
sol = noktalar[0]
for i in noktalar[::3]:
	if(sag < i):
		sag = i
	elif(sol > i):
		sol = i
buyukluk = 200/(sag - sol)
for i in range(0,len(noktalar)):
	noktalar[i] = noktalar[i] * buyukluk

# --------------------------------------------


def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-512, 512, -480, 480)

def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.8, 0.8, 1.0)

	# Drawing the model from different angles
	
	vektorelCizdir(0,2,-256, 240)
	vektorelCizdir(0,1, 256, 160)
	vektorelCizdir(2,1, -256, -240)
	vektorelCizdir(2, 0, 256, -240)
	
	# ---------------------------------------

	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(1024, 960)
glutInitWindowPosition(0,0)
glutCreateWindow("Tulga Renderer 0.0.1")
glutDisplayFunc(plotpoints)
init()
glutMainLoop()


dosya.close()
