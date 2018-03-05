
from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	i = 0
	funct = ""
	with open(fname) as file_object:
		for line in file_object:
			if i==0:
				#function names
				if line[:4] == "line":
					funct = "line"
				elif line[:5] == "ident":
					funct = 'ident'
				elif line[:5] == 'scale':
					funct = 'scale'
				elif line[:4] == 'move':
					funct = 'move'
				elif line[:6] == 'rotate':
					funct = 'rotate'
				elif line[:5] == 'apply':
					funct = 'apply'
				elif line[:6] == 'display':
					funct = 'display'
				elif line[:4] == 'save':
					funct = 'save'
			elif i == 1:
				if funct == "line":
					a = parse_args(6, line)
					add_edge(points, a[0], a[1], a[2], a[3], a[4], a[5])
				elif funct == "ident":
					funct = 'ident'
				elif funct == 'scale':
					funct = 'scale'
				elif funct == 'move':
					funct = 'move'
				elif funct == 'rotate':
					funct = 'rotate'
				elif funct == 'apply':
					funct = 'apply'
				elif funct == 'display':
					funct = 'display'
				elif funct == 'save':
					funct = 'save'
			
	return 0
def parse_args(index, string):
	list = []
	for i in range(index):
		list.append(string[:indexOf(" ")])
		string = string[indexOf(" ")+1:]
	return list