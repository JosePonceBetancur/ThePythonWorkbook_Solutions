#read the number of feet and read the number of inches
# 1 ft = 12 inch. 1 inch = 2.54 cm

ft , inch = int(input('Insert the number of feets you want to convert to cm: ')), int(input('Insert the number of inches you want to convert to cm: '))

def inch_to_cm(inches):
    return round((inches*2.54), 3)

def ft_to_inch(ft):
    return round((ft*12), 3)

print(f'{ft} ft is equal to {inch_to_cm(ft_to_inch(ft))} cm')

print(f'{inch} inch is equal to {inch_to_cm(inch)} cm')
