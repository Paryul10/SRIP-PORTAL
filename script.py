import re

script_1 = open("abc.txt", "r")

lines = script_1.readlines()
# print(lines[0])
lab = int(lines[0],10)
# print(lab)
a = []
b = []
c = []

aflag = 0
bflag = 0
cflag = 0

for line in lines:

	if re.match('JavaScript', line):
		a = line.split()
		aflag = 1
	if re.match('HTML', line):
		b = line.split()
		bflag = 1
	if re.match('CSS', line):
		c = line.split()
		cflag = 1

x = []
if aflag:
	x.append(a[0])
	x.append(a[-1])
if bflag:
	x.append(b[0])
	x.append(b[-1])
if cflag:
	x.append(c[0])
	x.append(c[-1])

# print(x)