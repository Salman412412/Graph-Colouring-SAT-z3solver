from z3 import *
borders={"Albania": ["Greece", "Kosovo", "Macedonia", "Montenegro"],
"Andorra": ["France", "Spain"],
"Austria": ["CzechRepublic", "Germany", "Hungary", "Italy", "Liechtenstein", "Slovakia","Slovenia", "Switzerland"],
"Belarus": ["Latvia", "Lithuania", "Poland", "Ukraine"],
"Belgium": ["France", "Germany", "Luxembourg", "Netherlands"],
"BosniaHerzegovina": ["Croatia", "Montenegro", "Serbia"],
"Bulgaria": ["Greece", "Macedonia", "Romania", "Serbia"],
"Croatia": ["BosniaHerzegovina", "Hungary", "Montenegro", "Serbia", "Slovenia"],
"Cyprus": [],
"CzechRepublic": ["Austria", "Germany", "Poland", "Slovakia"],
"Denmark": ["Germany"],
"Estonia": ["Latvia"],
"Finland": ["Norway", "Sweden"],
"France": ["Andorra", "Belgium", "Germany", "Italy", "Luxembourg", "Monaco", "Spain", "Switzerland"],
"Germany": ["Austria", "Belgium", "CzechRepublic", "Denmark", "France", "Luxembourg", "Netherlands", "Poland", "Switzerland"],
"Greece": ["Albania", "Bulgaria", "Macedonia"],
"Hungary": ["Austria", "Croatia", "Romania", "Serbia", "Slovakia", "Slovenia", "Ukraine"],
"Iceland": [],
"Ireland": ["UnitedKingdom"],
"Italy": ["Austria", "France", "SanMarino", "Slovenia", "Switzerland", "VaticanCity"],
"Kosovo": ["Albania", "Macedonia", "Montenegro", "Serbia"],
"Latvia": ["Belarus", "Estonia", "Lithuania"],
"Liechtenstein": ["Austria", "Switzerland"],
"Lithuania": ["Belarus", "Latvia", "Poland"],
"Luxembourg": ["Belgium", "France", "Germany"],
"Macedonia": ["Albania", "Bulgaria", "Greece", "Kosovo", "Serbia"],
"Malta": [],
"Moldova": ["Romania", "Ukraine"],
"Monaco": ["France"],
"Montenegro": ["Albania", "BosniaHerzegovina", "Croatia", "Kosovo", "Serbia"],
"Netherlands": ["Belgium", "Germany"],
"Norway": ["Finland", "Sweden"],
"Poland": ["Belarus", "CzechRepublic", "Germany", "Lithuania", "Slovakia", "Ukraine"],
"Portugal": ["Spain"],
"Romania": ["Bulgaria", "Hungary", "Moldova", "Serbia", "Ukraine"],
"SanMarino": ["Italy"],
"Serbia": ["BosniaHerzegovina", "Bulgaria", "Croatia", "Hungary", "Kosovo", "Macedonia","Montenegro", "Romania"],
"Slovakia": ["Austria", "CzechRepublic", "Hungary", "Poland", "Ukraine"],
"Slovenia": ["Austria", "Croatia", "Hungary", "Italy"],
"Spain": ["Andorra", "France", "Portugal"],
"Sweden": ["Finland", "Norway"],
"Switzerland": ["Austria", "France", "Germany", "Italy", "Liechtenstein"],
"Ukraine": ["Belarus", "Hungary", "Moldova", "Poland", "Romania", "Slovakia"],
"UnitedKingdom": ["Ireland"],
"VaticanCity": ["Italy"]}

s=Solver()

countries=borders.keys()
countries_total=len(countries)

country_color=[Int('country%d_color' % c) for c in range(countries_total)]
print(country_color)

for i in range(countries_total):
	s.add(country_color[i]>=0)
	s.add(country_color[i]<4)

def country_name_to_idx(s):
	return list(countries).index(s)

for i in range(countries_total):
	for b in borders[list(countries)[i]]:
		s.add(country_color[i] != country_color[country_name_to_idx(b)])

print(s.check())
m=s.model()

#for i in range(countries_total):
# print m[country_color[i]].as_long()

print("coloring={")
for i in range(countries_total):
	color=m[country_color[i]].as_long()
	if color==0:
		s="1,0,0"
	elif color==1:
		s="0,1,0"
	elif color==2:
		s="0,0,1"
	elif color==3:
		s="1,1,0"
	print("\tEntity[\"Country\", \""+list(countries)[i]+"\"] -> RGBColor["+s+"], ")
print("}")
