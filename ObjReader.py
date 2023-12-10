# Coded by Enes Tulga
# You can test the code with your own OBJ Files. But I do not guarantee for the best performance.

# IMPORTING GL LIBRARIES

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# -------------------------

# Reading OBJ files
objFile = open("ObjFiles/Centaur.obj", "r")	# Give the first parameter as obj file directory.
model = objFile.read()
# ------------------------------

vertices = []   # Verticies
faces = []	# Faces

#  The Function that finds verticies in model variable (obj file) and assign to vertices array
def FindVertices():
	global model
	global vertices
	i = 0
	lineString = ""
	flag = False
	while(i < len(model)):
		if(flag):
			flag = False
			if(model[i] == 'v' and model[i + 1] == " "):
				i += 1
				
				while(model[i] != "\n"):
					if(model[i] != " "):
						lineString += model[i]
						i += 1
						if(model[i] == " " or model[i] == "\n"):
							
							vertices.append(float(lineString))
							lineString = ""
							
					else:
						i += 1
				continue			
		if(model[i] == "\n"):
			flag = True
		i += 1

#  The Function that finds faces in model variable (obj file) and assign to faces array
def FindFaces():
	global model
	global faces
	i = 0
	lineString = ""
	vertexArrayInLine = []
	flag = False
	while(i < len(model)):
		if(flag):
			flag = False
			if(model[i] == 'f' and model[i + 1] == " "):
				
				i += 1
				
				while(model[i] != "\n"):
					if(model[i] != " "):
						lineString += model[i]
						i += 1
						
						if(model[i] == "/"):
							vertexArrayInLine.append(int(lineString) - 1)
							lineString = ""
							while(model[i] != " " and model[i] != "\n"):
								i += 1
						if(model[i] == "\n" or model[i + 1] == "\n"):
							
							faces.append(vertexArrayInLine)
							vertexArrayInLine = []
					else:
						i += 1				
		if(model[i] == "\n"):
			flag = True
		i += 1


# This function drawing 3D model in faces and vertices arrays in angle depends on a and b parameter.
#	a = {0 : X, 1: Y, 2: Z}
#	b = {0 : X, 1: Y, 2: Z}
#    Also, x and y parameter defines that where is the starting of the frame. 
def DrawMesh(a,b, x, y):
	for face in faces:
		glBegin(GL_POLYGON)
		for vertex in face:
			glVertex2f(vertices[vertex*3 + a] + x, vertices[vertex*3 + b] + y)
		glEnd()
FindVertices()
FindFaces()

# SCALING MODEL

mostRightVertex = vertices[0]
mostLeftVertex = vertices[0]
for i in vertices[::3]:
	if(mostRightVertex < i):
		mostRightVertex = i
	elif(mostLeftVertex > i):
		mostLeftVertex = i
scaleRatio = 200/(mostRightVertex - mostLeftVertex)
for i in range(0,len(vertices)):
	vertices[i] = vertices[i] * scaleRatio

# --------------------------------------------


def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-512, 512, -480, 480)

def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.8, 0.8, 1.0)

	# Drawing the model from different angles
	
	DrawMesh(0,2,-256, 240)
	DrawMesh(0,1, 256, 160)
	DrawMesh(2,1, -256, -240)
	DrawMesh(2, 0, 256, -240)
	
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


objFile.close()
