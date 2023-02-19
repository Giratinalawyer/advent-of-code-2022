data = open('6.in').read()
lines = [x for x in data.split('\n')]
print(data)
print(lines)
for i in range(len(data)):
    if i > 2:
        letters = set(data[i-4:i])
        if len(letters) == 4:
            print("part 1:", i)
            break

for i in range(len(data)):
    if i > 2:
        letters = set(data[i-14:i])
        if len(letters) == 14:
            print("part 2:", i)
            break

# # 16 minutes. meh. Good to know about sets.


#nthistle solution:
# with open("6.in") as f:
#     s = f.read().strip()

# s1 = s
# i = 0
# while len(set(s1[:4])) != 4:
#     s1 = s1[1:]
#     i += 1
# print(i+4)

# s2 = s
# i = 0
# while len(set(s2[:14])) != 14:
#     s2 = s2[1:]
#     i += 1
# print(i+14)

# Jonathan Paulson solution
data = open('6.in').read()
lines = [x for x in data.split('\n')]

p1 = False
p2 = False
for i in range(len(data)):
    if (not p1) and i-3>=0 and len(set([data[i-j] for j in range(4)]))==4:
        print(i+1)
        p1 = True
    if (not p2) and i-13>=0 and len(set([data[i-j] for j in range(14)]))==14:
        print(i+1)
        p2 = True