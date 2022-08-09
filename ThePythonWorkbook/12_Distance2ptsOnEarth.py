# distance = 6371.01 * arccos(sin(t1))*sin(t2)+cos(t1)*cos(t2)*cos(g1 - g2))

import math


#latitude = t
#longitude = g 

# point 1:
t1 , g1 = math.radians(float(input('Insert the latitude of the first point: '))) , math.radians(float(input('Insert the longitude of the first point: ')))
# point 1:
t2 , g2 = math.radians(float(input('Insert the latitude of the second point: '))) , math.radians(float(input('Insert the longitude of the second point: ')))

earth_radius = 6371.01

distance = earth_radius * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2)) 

print(f'The distance between the two points you write is {round(distance, 3)} [km].')
