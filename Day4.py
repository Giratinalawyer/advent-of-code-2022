# Advent of Code 2022 Day 4

f = [l.strip() for l in open('Day4Input.txt')]

p1 = 0
p2 = 0
for l in f:

    a = l.split(",")
    b = a[0].split("-")
    c = a[1].split("-")
    b[0] = int(b[0])
    b[1] = int(b[1])
    c[0] = int(c[0])
    c[1] = int(c[1])
    if (b[0] <= c[0] and b[1] >= c[1]) or (b[0] >= c[0] and b[1] <= c[1]):
        p1 += 1
    # if (c[1] >= b[0] and c[0] <= b[1]):
    # either if statement works; second one was a bit more obvious to me, though first is just negation
    # (didn't think of this neater way until after - had ugly one of four ors of ands during)
    if not(b[1] < c[0] or b[0] > c[1]):
        p2 += 1

print("part 1 is", p1)
print("part 2 is", p2)

# 20 minutes for part 1, 10 minutes for part 2

# Jonathan Paulson's solution for day 4:
# import sys
# infile = sys.argv[1] if len(sys.argv)>1 else '4.in'
# data = open(infile).read().strip()
# lines = [x.strip() for x in data.split('\n')]
# p1 = 0
# p2 = 0
# for line in lines:
#     one,two = line.split(',')
#     s1,e1= one.split('-')
#     s2,e2= two.split('-')
#     s1,e1,s2,e2 = [int(x) for x in [s1,e1,s2,e2]]
#     # (s2,e2) is fully contained in (s1,e1) if s1<=s2 and e2<=e1
#     if s1<=s2 and e2<=e1 or s2<=s1 and e1<=e2:
#         p1 += 1
#     # (s2,e2) overlaps (s1,e1) if it is not completely to the left or completely to the right
#     #          s2 -- e2
#     #    e1              s1
#     if not (e1 < s2 or s1 > e2):
#         p2 += 1
# print(p1)
# print(p2)