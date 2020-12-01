square = {2: 4, 3: 9, -1: 1, -2: 4}

# the smallest key
key1 = min(square)
print("The smallest key:", key1)    # -2

# the key whose value is the smallest
key2 = min(square, key = lambda k: square[k])

print("The key with the smallest value:", key2)    # -1

# getting the smallest value
print("The smallest value:", square[key2])    # 1

from collections import OrderedDict

dict = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

############################################################################################
for i in sorted(dict.keys()):
    print(dict[i])

########## sorted values ##################################################################################


dict1 = {1: 'a', 2: 'd', 3: 'c'}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]

print("asas",sorted_keys)

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}


##########################################################


dict1 = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}
sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
sorted_dict = {k: v for k, v in sorted_tuples}

print(sorted_dict)  # {1: 1, 3: 4, 2: 9}

##########################################################
mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key in sorted(mydict):
    print(key, mydict[key])