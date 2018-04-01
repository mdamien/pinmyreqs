# unpinmyreqs requirements.txt

# TODO: cmd line help / click
# asciinema
import sys, re

for line in open(sys.argv[1]):
	line = line.strip()
	m = re.match('([\w\d\-\_\.]+)==([\w\d\.]+)', line)
	if m:
		print(m.group(1))
	else:
		print(line)