import sys, re

# TODO: cmd line help / click
# asciinema

def pinmyreqs():
	# pip freeze | pinmyreqs requirements.txt
	# TODO: pin the unpinned
	freezed = {}
	for line in sys.stdin:
		line = line.strip()
		if line and not line.startswith('-e '):
			m = re.match('([\w\d\-\_\.]+)==([\w\d\.]+)', line)
			if m:
				pkg, version = m.groups()
				freezed[pkg] = version
			else:
				print('Invalid line:', line, file=sys.stderr)

	for line in open(sys.argv[1]):
		line = line.strip()
		m = re.match('([\w\d\-\_\.]+)==([\w\d\.]+)', line)
		if m:
			pkg, version = m.group(1), m.group(2)
			if pkg in freezed:
				print('%s==%s' % (pkg, freezed[pkg]))
			else:
				print(line)
		else:
			print(line)


def unpinmyreqs():
	for line in open(sys.argv[1]):
		line = line.strip()
		m = re.match('([\w\d\-\_\.]+)==([\w\d\.]+)', line)
		if m:
			print(m.group(1))
		else:
			print(line)