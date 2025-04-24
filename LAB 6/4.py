import operator
lp = [("i1",10),("i2",20),("i3",30),("i4",5)]
print (sorted(lp, key = operator.itemgetter(1), reverse = True))
          