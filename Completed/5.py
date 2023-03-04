# Advent of Code 2022 Day 5

from copy import deepcopy

f = []
g = open('5.in')
h = []
i = 0

while i < 8:
    f.append(g.readline())
    print(f[i])
    i += 1

i = 0
for j in range(9):
    if f[7][i+1] != " ":
        h.append(f[7][i+1])
        i +=4
        h[j] = list(h[j])

print(h, "\n\n")
j = 6
while j > -1:
    i = 0
    for k in range(9):
        if f[j][i+1] != " ":
            h[k].append((f[j][i+1]))
        i +=4
    j -= 1

p2 = deepcopy(h)

f = [l.strip() for l in open('5.in')]

k = 10
for l in f[10:]:
    a = f[k].split()
    k += 1
    for i in range(int(a[1])):
        h[int(a[5])-1].append(h[int(a[3])-1].pop())
        p2[int(a[5])-1].append(p2[int(a[3])-1].pop(-int(a[1])+ i))

b = ""
for j in range(9):
    b = b + (h[j][-1])
q = ""
for j in range(9):
    q = q + (p2[j][-1])

print("answer to part 1:", b)
print("answer to part 2:", q)

g.close()


# 1 solution from reddit thread: - don't forget to remove your a

# def parse_stack_text(stacktext):
#     stacks = [""]*10
#     for line in stacktext[:-1]:
#         for i, box in enumerate(line[1::4]):
#             if box != " ": stacks[i+1] += box
#     return stacks
    
# input_data = open("data05.txt").read()
# stackt, instructions = [part.split("\n") for part in input_data.split("\n\n")]
# stacks = parse_stack_text(stackt)

# p1, p2 = stacks[:], stacks[:]
# for line in instructions:
#     _, n, _, src, _, dest = line.split()
#     n = int(n); src = int(src); dest = int(dest)

#     p1[src], p1[dest] = p1[src][n:],  p1[src][:n][::-1] + p1[dest]
#     p2[src], p2[dest] = p2[src][n:],  p2[src][:n]       + p2[dest]

# print("Part 1:", "".join(s[0] for s in p1 if s))
# print("Part 2:", "".join(s[0] for s in p2 if s))

# demonstration of Paulson's data reading technique:
# data = open('5.in').read()
# lines = [x for x in data.split('\n')]
# print(data)
# print(lines)