from display import *
from draw import *
from matrix import *
def parse_file( fname, points, transform, screen, color ):
	with open(fname) as file_object:
		script = file_object.read().split()
		#print(script)
		#while there is stuff to execute
		index = 0
		while index < len(script):
			#commands
			#line
			#x0 y0 z0 x1 y1 z1
			if script[index] == 'line':
				add_edge(points, int(script[index+1]), int(script[index+2]), int(script[index+3]),
				int(script[index+4]), int(script[index+5]), int(script[index+6]))
				index+=7
			elif script[index] == 'ident':
				ident(transform)
				index+=1
			elif script[index] == 'scale':
				matrix_mult(make_scale(int(script[index+1]), int(script[index+2]), int(script[index+3])), transform)
				index+=4
			elif script[index] == 'move':
				matrix_mult(make_translate(int(script[index+1]),int(script[index+2]), int(script[index+3])), transform)
				index+=4
			elif script[index] == 'rotate':
				if script[index+1]=='x':
					matrix_mult(make_rotX(int(script[index+2])), transform)
					index+=3
				elif script[index+1]=='y':
					matrix_mult(make_rotY(int(script[index+2])), transform)
					index+=3
				elif script[index+1]=='z':
					matrix_mult(make_rotZ(int(script[index+2])), transform)
					index+=3
			elif script[index] == 'apply':
				#print_matrix(points)
				matrix_mult(transform, points)
				ftoi(points)
				
				index+=1
			elif script[index] == 'display':
				draw_lines(points, screen, color)
				display(screen)
				index+=1
			elif script[index] == 'save':
				draw_lines(points, screen, color)
				save_ppm(screen, script[index+1])	
				index+=2
			else:
				index+=1
			#update the string
	pass
def ftoi(matrix):
	for c in range(len(matrix)):
		for r in range(len(matrix[0])):
			matrix[c][r]= int(matrix[c][r])
tm = new_matrix()
pm = []
screen = new_screen()
color = [ 0, 255, 0 ]
parse_file('script', pm, tm, screen, color)
