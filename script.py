import re

script_1 = open("abc.txt", "r")

for line in script_1:

	if re.match('JavaScript', line):

		a = line.split()

	if re.match('HTML', line):

		b = line.split()

	if re.match('CSS', line):

		c = line.split()

x = [a[0], a[-1], b[0], b[-1], c[0], c[-1]]