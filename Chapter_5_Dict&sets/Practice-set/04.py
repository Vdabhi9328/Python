s = set()

s.add(20)
s.add(20.0)
s.add('20')

print(s)       # {'20', 20}
print(len(s)) # length = 2

#----problem - 5 -----
d = {}
print(type(d))  # dict