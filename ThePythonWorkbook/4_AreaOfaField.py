# Input of the width and the length
width = float(input('What is the width of your farm (in ft)?: '))
length = float(input('What is the length of your farm (in ft)?: '))

# 43560 square feet = acre

# Computing
area = width * length #in square feet
area_acre = area/43560

print(f'The area of your farm is {area_acre} acres')

