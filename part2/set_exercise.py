#1
gryffindor = set(["Potter", "Weasley", "Granger", "Longbottom", "Finnigan"])
slytherin = set(["Riddle", "Malfoy", "Snape", "Baron"])
ravenclaw = set(["Lovegood", "Lockhart", "Trelawney"])

#2
gryffindor_slytherin = gryffindor.union(slytherin)

#3
gryffindor_ravenclaw = gryffindor.union(ravenclaw)

#4
together = gryffindor_slytherin.intersection(gryffindor_ravenclaw)

#5
print(together)
