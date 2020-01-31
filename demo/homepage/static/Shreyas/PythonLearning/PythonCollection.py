# Four Datatype are present fro Data Collecetion
# List, Dict, Tuple & Set

# Python has InBuilt Collection Library also called 'import collections'
# different collections are :- namedtuple(), Chainmap, deque, Counter, OrderDict, defaultdict,  UserDict, UserString,
# UserString

from collections import namedtuple, deque, Counter, OrderedDict

# namedtuple() is helpful because it stores the value in name given, no need to remember the index value
data1 = namedtuple("User_Info", "name, surname")  # UserInfo is name of namedtuple & firstname & lastname
# is varibale named to store the data
data1_1 = data1("Shreyas", "AMbre")
print(data1_1)

s = data1._make(["Sujata", "Ambre"])
print(s)

# deque() is one type of inbuilt collection in python for optimise the list to perfomr insertion & deletion

a = ["s", "h", "r", "e", "y", "a", "s"]
d = deque(a)
d.append("Python ")  # it append the value at last position
print(d)
d.appendleft("Tutorail")
print(d)
d.popleft()
print(d)

# ***********************Chainmap*****************************************************************
# Chainmap is dictionary like class for creating single view of multiple mapping
# in simple term we can initialize multiple dictionary in single Chainmap
#
# c = {"skill": "Python", "experience": 1}
# d = {"company": "IBM" , "Function": "Software Developer"}
#
# z = ChainMap(c, d)
# print(z)

# ************************Counter * **********************************
# counter is dictionary subclass for counting hashable objects
# Counter works to tell programmer how many time the number(any values) is occured in the list in key value pair
# output:- value given by users: how many times value is repeayed Counted Value printed

numbers = [1,2,3,1,2,4,5,3,4,1,3,5,6,1,1,2,3]
count = Counter(numbers)
print(count)


# *********************** OrderDict *******************
d = OrderedDict()
d[1] = 's'
d[2] = 'h'
d[3] = 'r'
d[4] = 'e'

print(d)


