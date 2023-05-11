#Create an empty Set
land_features = set()

#Add some elements to the set
land_features.add("tree")
land_features.add("waterfall")
land_features.add("lake")
land_features.add("pond")
land_features.add("lava")
land_features.add("lava")
#we can add duplicates but only one is saved
land_features.add("volcano")
land_features.add("volcano")

print(land_features)

#We can check if an element is in the set this way
if "lake" in land_features:
    print("Lake is in the set")
else:
    print("Not in the set")

#Remove the element pond from the set
land_features.remove("pond")
print(land_features)

#We can iterate over all the items
for features in land_features:
    print(features)