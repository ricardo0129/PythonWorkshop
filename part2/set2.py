#create two sets with shapes on each one
shapes_1 = set(['circle', 'square', 'triangle'])
shapes_2 = set(['trapezoid', 'rectangle', 'triangle', 'square'])

#create a new set with the two sets combined
shapes_union = shapes_1.union(shapes_2)
print(shapes_union)

#only keep elements that are in both sets
shapes_intersection = shapes_1.intersection(shapes_2)
print(shapes_intersection)

#store elements that are in shape_1 but not in shape_2
shapes_diff_1 = shapes_1.difference(shapes_2)
print(shapes_diff_1)
