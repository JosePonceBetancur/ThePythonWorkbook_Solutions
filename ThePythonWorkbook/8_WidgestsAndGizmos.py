# Each gizmo 112g and each widget 75g

widgets = int(input('Insert the number of widgets of the order: '))
gizmo = int(input('Insert the number of gizmo of the order: '))

widgets_weight = widgets * 75
gizmo_weight = gizmo * 112

print(f'The total weight of your order is {int(widgets_weight) + int(gizmo_weight)} g')


