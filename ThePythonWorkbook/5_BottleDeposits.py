# 0,10 for = 1L and 0.25 if > 1L

drink_1L = float(input('How many drink containers of 1L did you return?: '))
drink_moreThan1L = float(input('How many drink containers of more than 1L did you return?: '))

deposit_1L = drink_1L*0.10
deposit_moreThan1L = drink_moreThan1L * 0.25 

total_deposit = deposit_1L + deposit_moreThan1L 

print(f'Your deposit is ${round(total_deposit, 2)}')
