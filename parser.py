from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
	i = 0
	funct = ""
	with open(fname) as file_object:
		for line in file_object:
			if i==0:
				#function names
				if line[:4] == "line":
					funct = "line"
					i = 1
				elif line[:5] == "ident":
					ident(transform)
				elif line[:5] == 'scale':
					funct = 'scale'
					i = 1
				elif line[:4] == 'move':
					funct = 'move'
					i = 1
				elif line[:6] == 'rotate':
					funct = 'rotate'
					i = 1
				elif line[:5] == 'apply':
					matrix_mult(transform, points)
				elif line[:7] == 'display':
					con(points)
					draw_lines(points, screen, color)
				elif line[:4] == 'save':
					funct = 'save'
					i = 1
				elif line[:4] == 'quit':
					return
			elif i == 1:
				if funct == "line":
					a = parse_args(6, line)
					for i in range(6):
						a[i] = 0 + int(a[i])
					add_edge(points, a[0], a[1], a[2], a[3], a[4], a[5])
					i = 0
				elif funct == 'scale':
					a = parse_args(3, line)
					for i in range(3):
						a[i] = 0 + int(a[i])
					matrix_mult(make_scale(a[0], a[1], a[2]), transform)
					i = 0
				elif funct == 'move':
					a = parse_args(3, line)
					for i in range(3):
						a[i] = 0 + int(a[i])
					matrix_mult(make_translate(a[0], a[1], a[2]), transform)
					i = 0
				elif funct == 'rotate':
					a = parse_args(2, line)
					a[1] = 0 + int(a[i])
					if a[0] == 'x':
						matrix_mult(make_rotX(a[1]), transform)
					elif a[0] == 'y':
						matrix_mult(make_rotY(a[1]), transform)
					elif a[0] == 'z':
						matrix_mult(make_rotZ(a[1]), transform)
					i = 0
				elif funct == 'save':
					a = parse_args(1, line)
					con(points)
					draw_lines(points, screen, color)
					save_ppm(screen, a[0])
					i = 0

	pass

def parse_args(index, string):
	list = []
	for i in range(index):
		if i != index - 1:
			list.append(string[:string.index(" ")])
			string = string[string.index(" ")+1:]
		else:
			list.append(string[:string.index("\n")])
	return list
def con(matrix):
	for i in range(len(matrix)):
		for c in range(len(matrix[0])):
			matrix[i][c] = 0 + int(matrix[i][c])

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()	

parse_file('script', edges, transform, screen, color)
print_matrix(edges)
