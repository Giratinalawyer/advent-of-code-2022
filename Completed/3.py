# Advent of Code 2022 Day 3

f = [l.strip() for l in open('Day3Input.txt')]

def main():
    p1 = 0
    p2 = 0
    i = 0
    for entry in f:
        for char in f[i][:len(entry)//2]:
            if char in f[i][len(entry)//2:]:
                if char.isupper():
                    p1 += ord(char)-38
                    break
                elif char.islower():
                    p1 += ord(char)-96
                    break
        i += 1
    print("the answer to part 1 is", p1)
    i = 0
    for j in range(len(f)//3):
        for char in f[i]:
            if char in f[i+1] and char in f[i+2]:
                if char.isupper():
                    p2 += ord(char)-38
                    break
                elif char.islower():
                    p2 += ord(char)-96
                    break
        i += 3
    print("the answer to part 2 is", p2)

main()

# Jonathan Paulson's solution
# def score(c):
#     if 'a'<=c<='z':
#         return ord(c)-ord('a') + 1
#     else:
#         return ord(c)-ord('A') + 1 + 26


# p1 = 0
# for line in open('3.in'):
#     x = line.strip()
#     assert len(x)%2 == 0
#     y,z = x[:len(x)//2], x[len(x)//2:]
#     for c in y:
#         if c in z:
#             p1 += score(c)
#             break
# print(p1)

# p2 = 0
# X = [line for line in open('3.in')]
# i = 0
# while i < len(X):
#     for c in X[i]:
#         if c in X[i+1] and c in X[i+2]:
#             p2 += score(c)
#             break
#     i += 3
# print(p2)