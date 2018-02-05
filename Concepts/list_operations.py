list = [77, 66, 89, 12, 34, 56, 93]

# sorted will not change the origial list
print sorted(list)
print list

# does not return any value, but changes the original list
list.sort()
print list


print list.pop(-1)
print list


print 100**100