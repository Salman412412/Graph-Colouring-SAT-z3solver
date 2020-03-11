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
with open('SampleGraph.txt', 'r') as f:
    lines = f.read().splitlines()
	
node_number = 0
edge_number = 0
for line in lines:
	edge_number = edge_number + 1
	if int(line.split()[1]) > node_number:
		node_number = int(line.split()[1])
print('Number of nodes: ' + str(node_number))
print('Number of edges: ' + str(edge_number))
print('\n')

# Ijade graph array
Garray = np.zeros((node_number,node_number),dtype=bool)
GarrayNo = np.zeros((node_number,1),dtype=int)

for line in lines:
	first_node = int(line.split()[0])
	second_node = int(line.split()[1])
	Garray[first_node-1, second_node-1] = True
	GarrayNo[first_node-1,0] = GarrayNo[first_node-1,0] + 1
	Garray[second_node-1, first_node-1] = True
	GarrayNo[second_node-1,0] = GarrayNo[second_node-1,0] + 1


# Morattabsazi Array nesbat be te'dade yalha
for i in range(node_number):
	for j in range(i+1, node_number):
		if GarrayNo[j,0] > GarrayNo[i,0]:
			GarrayNo[i,0], GarrayNo[j,0] = GarrayNo[j,0], GarrayNo[i,0]
			Garray[[i,j]] = Garray[[j,i]]
			Garray[:,[i, j]] = Garray[:,[j, i]]



# Halghe baraye peyda kardane hadde aghalle range
lower_band = 1
upper_band = node_number - 1
start = datetime.now()

while (upper_band > (lower_band+1)):
	ColorNo = (upper_band+lower_band)//2
	# Ta'rife moteghayyerha
	Gcolor =[[Bool('Node_no%d_c%d' % (r+1,c+1)) for c in range(ColorNo)] for r in range(node_number)]
	# Ta'rife solver
	s = Solver()
	print('Testing ' + str(ColorNo)+ ' Colour(s)')
	
	#Sharte yeksan nabudane range yalhaye mojaver
	for i in range(node_number):
		for j in range(i, node_number):
			if Garray[i,j]:
				for k in range(ColorNo):
					s.add(And(Gcolor[i][k],Gcolor[j][k]) == False)
					
	#Sharte dashtane yek rang baraye har node_number
	for i in range(node_number):
		for k in range(ColorNo):
			for h in range(k,ColorNo):
				if k != h:
					s.add(And(Gcolor[i][k],Gcolor[i][h]) == False)
					
	#Sharte rang dashtane har node
	for i in range(node_number):
		s.add(Or([Gcolor[i][c] for c in range(ColorNo)]) == True)

	#Check kardane emkane vojude javab
	if s.check() == unsat:
		print('Not Satisfied')
		lower_band = ColorNo
	else:
		print('Satisfied')
		upper_band = ColorNo
	print('Time till now: '+ str(datetime.now()-start))
	print('\n')

		
#Namayeshe Natayej
print('\n')
print('The calculation time is: ' + str(datetime.now()-start))
print('The minimum number of Colours: ' + str(ColorNo))
print('\n')
