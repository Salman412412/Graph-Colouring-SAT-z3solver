from datetime import datetime

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
last_line = lines[-1]
node_number = int(last_line.split()[0])

# Ijade graph array
Garray = np.zeros((node_number,node_number),dtype=bool)
Gcolor = [Int('Node%d_color' % (c+1)) for c in range(node_number)]

for line in lines:
	first_node = int(line.split()[0])
	second_node = int(line.split()[1])
	Garray[first_node-1, second_node-1] = True

# Morattabsazi Array nesbat be te'dade yalha

start = datetime.now()
for ColorNo in range(node_number):
	# Ta'rife solver
	s = Solver()
	
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
		break

#Namayeshe Natayej
print('The calculation time is: ' + str(datetime.now()-start))
print('The minimum number of Colours: ' + str(ColorNo))
