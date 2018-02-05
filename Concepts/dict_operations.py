t_dict = {'name': 'xyz', 'age': 27, 's': 'l1'}
temp = {'ID': 1223456}

t_list = [1, 2, 3, 4, 5]

'''
dict.update(other_dict)
dict.has_key(key) - returns true of false
dict.get(key)
'''
t_dict.update(temp)

print t_dict

print "Length {}".format(len(t_dict))
print "Type {}".format(type(t_dict))

if t_dict.has_key('name'):
    print "True"

print t_dict.get('')

print t_dict['name']
# the below line returns a key error
# print t_dict['game']

print t_dict.get('name')
print t_dict.get('game') # this line returns None, if k=the key is not present

print t_dict.keys()
print t_dict.values()


# print t_dict.items()

for key, value in t_dict.items():
    print key + " -> " + str(value)