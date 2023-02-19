# Advent of Code 2022 Day 1

f = open('Day1ElfCalories.txt','r')
list = ""
elfCalories = []
i = 0
while True:
    a = f.readline()
    if a == "":
        break
    list = list + a
    i += 1
b = []
b = list.split("\n\n")
d = []
for i in range(len(b)):
    c = b[i].split("\n")
    j = 0
    e = []
    for j in range(len(c)):
        if c[j] == "":
            break
        e.append(int(c[j]))
    d.append(sum(e))
print("the calories carried by the elf with the most is", max(d))
totCal = max(d)
d.pop(d.index(max(d)))
print(max(d))
totCal += max(d)
d.pop(d.index(max(d)))
print( max(d))
totCal += max(d)
print("the number of calories carried by the three elves with the most is", totCal)
f.close()


# Abe's version:
# def main():
#      with open("Calories.txt","r") as f:
#          lines = f.readlines()
#          calories = [entry.strip() for entry in lines]
#      elf_sums=[]
#      current_sum = 0
#      for entry in calories:
#           if entry != '':
#               current_sum += int(entry)
#           elif entry == '':
#               elf_sums.append(current_sum)
#               current_sum = 0
#      elf_sums.append(current_sum)
#      max_cals = max(elf_sums)
#      print(max_cals)
# main()

# # Cool eval way from guy on reddit thread:
# f = sorted(eval(open('in.txt').read().
#     replace('\n\n', ',').replace('\n', '+')))

# print(f[-1], sum(f[-3:]))

# #other cool reddit guy (Jonathan Paulson):
# X = [l.strip() for l in open('1.in')]

# Q = []
# for elf in ('\n'.join(X)).split('\n\n'):
#     q = 0
#     for x in elf.split('\n'):
#         q += int(x)
#     Q.append(q)
# Q = sorted(Q)
# print(Q[-1])
# print(Q[-1]+Q[-2]+Q[-3])