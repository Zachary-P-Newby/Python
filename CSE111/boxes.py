from math import ceil

#Get items
n_items = int(input("How many items do you have? "))
items_per_box = int(input("How many items will you pack per box? "))

#calculate boxes
boxes_needed = n_items / items_per_box
boxes_needed = ceil(boxes_needed)

#print result:
print()
print(f"You will need {boxes_needed} boxes to fit {n_items} items at {items_per_box} items per box.")