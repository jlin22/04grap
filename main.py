from display import *
from draw import *
from matrix import *
from parser import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parser.parse_file( 'script', edges, transform, screen, color )