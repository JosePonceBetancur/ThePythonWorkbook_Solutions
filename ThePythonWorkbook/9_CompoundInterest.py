init_balance = float(input('How much money do you want to deposit here?: '))

first_year_balance = init_balance + (0.04 * init_balance)
second_year_balance = (0.04*first_year_balance) + first_year_balance
third_year_balance = (0.04*second_year_balance) + second_year_balance

print(f'In the first year you will get: ${round(first_year_balance, 2)}')
print(f'In the second year you will get: ${round(second_year_balance, 2)}')
print(f'In the third year you will get: ${round(third_year_balance, 2)}')
