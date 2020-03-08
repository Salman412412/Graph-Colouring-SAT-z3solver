from datetime import datetime
from os import system

system('cls')

# Import kardane tamame functions az z3
# Baraye nasbe z3 solver be adrese zir moraje'e konid:
# https://github.com/Z3Prover/z3
from z3 import *

# Import kardane NumPy
# Baraye nasb az dature pip install NumPy estefade konid.
import numpy as np

# Baz kardane file graph
with open('g12518.txt', 'r') as f:
    lines = f.read().splitlines()
	
node_number = 0;
for line in lines:
	if int(line.split()[1]) > node_number:
		node_number = int(line.split()[1])
print('Number of nodes: ' + str(node_number))
print('\n')


# Ijade graph array
Garray = np.zeros((node_number,node_number),dtype=bool)
GarrayNo = np.zeros((node_number,1),dtype=int)
Gcolor = [Int('Node%d_color' % (c+1)) for c in range(node_number)]

for line in lines:
	first_node = int(line.split()[0])
	second_node = int(line.split()[1])
	Garray[first_node-1, second_node-1] = True
	GarrayNo[first_node-1,0] = GarrayNo[first_node-1,0] + 1

# Morattabsazi Array nesbat be te'dade yalha
for i in range(node_number):
	for j in range(i+1, node_number):
		if GarrayNo[j,0] > GarrayNo[i,0]:
			GarrayNo[i,0], GarrayNo[j,0] = GarrayNo[j,0], GarrayNo[i,0]
			Garray[[i,j]] = Garray[[j,i]]

start = datetime.now()
for ColorNo in range(node_number):
	# Ta'rife solver
	s = Solver()
	print('Testing ' + str(ColorNo+1)+ ' Colour(s)')
	
	#Sharte Te'dade Rangha
	for i in range(node_number):
		s.add(Gcolor[i]>=1)
		s.add(Gcolor[i]<(ColorNo+1))
	
	#Sharte yeksan nabudane range yalhaye mojaver
	for i in range(node_number):
		for j in range(node_number):
			if Garray[i,j]:
				s.add(Gcolor[i] != Gcolor[j])
	
	#Check kardane emkane vojude javab
	if s.check() == sat:
		print('Satisfied')
		break
	else:
		print('Not Satisfied')
		print('Time till now: '+ str(datetime.now()-start))
		print('\n')

#Namayeshe Natayej
print('The calculation time is: ' + str(datetime.now()-start))
print('The minimum number of Colours: ' + str(ColorNo))
