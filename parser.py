from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
	i = 0
	funct = ""
	with open(fname) as file_object:
		for line in file_object:
			if i==0:
				i = (i+1)%2
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
				elif line[:4] == 'quit':
					funct = 'quit'
			elif i == 1:
				if funct == "line":
					a = parse_args(6, line)
					add_edge(points, a[0], a[1], a[2], a[3], a[4], a[5])
					i = (i + 1) % 2
				elif funct == "ident":
					ident(transform)
				elif funct == 'scale':
					a = parse_args(3, line)
					matrix_mult(make_scale(a[0], a[1], a[2]), transform)
					i = (i + 1) % 2

				elif funct == 'move':
					a = parse_args(3, line)
					matrix_mult(make_translate(a[0], a[1], a[2]), transform)
					i = (i + 1) % 2
				elif funct == 'rotate':
					i = (i + 1) % 2
					a = parse_args(2, line)
					if a[0] == 'x':
						matrix_mult(make_rotX(a[1]), transform)
					elif a[0] == 'y':
						matrix_mult(make_rotY(a[1]), transform)
					elif a[0] == 'z':
						matrix_mult(make_rotZ(a[1]), transform)

				elif funct == 'apply':
					matrix_mult(transform, points)
				elif funct == 'display':
					draw_lines(points, screen, color)
					display(screen)
				elif funct == 'save':
					a = parse_args(1, line)
					draw_lines(points, screen, color)
					save_extension(screen, "img.jpg")
				elif funct == 'quit':
					return
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


screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
parse_file( 'script', edges, transform, screen, color )
print_matrix(edges)
