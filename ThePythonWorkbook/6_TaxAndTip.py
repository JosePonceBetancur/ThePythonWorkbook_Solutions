cost_meal = float(input('What was the cost of your meal?: '))

meal_tax = cost_meal * 0.19
meal_tip = cost_meal * 0.18 

print(f'The tax is ${round(meal_tax, 2)}')
print(f'The tip is ${round(meal_tip, 2)}')
print(f'The total amount is ${round((cost_meal + meal_tax + meal_tip), 2)}')




