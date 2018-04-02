import sys
import re

# TODO use rparse

RE_PKG = r'([\w\d\-\_\.]+)(?:==([\w\d\.]+))?'


def pinmyreqs():
    if len(sys.argv) != 2 or sys.stdin.isatty():
        print('usage: pip freeze | pinmyreqs requirements.txt', file=sys.stderr)
        return -1

    # TODO: pin the unpinned
    # TODO -e git+git@github.com:XXXX
    freezed = {}
    for line in sys.stdin:
        line = line.strip()
        parsed = False
        if line:
            m = re.match(RE_PKG, line)
            if m:
                pkg, version = m.groups()
                if version:
                    freezed[pkg.lower()] = version
                    parsed = True
            if not parsed:
                print('[warning] ignored pip-freeze line:', '`' + line + '`', file=sys.stderr)

    for line in open(sys.argv[1]):
        line = line.strip()
        m = re.match(RE_PKG, line)
        parsed = False
        if m:
            pkg = m.group(1)
            if pkg.lower() in freezed:
                print('%s==%s' % (pkg, freezed[pkg.lower()]))
            else:
                print('[warning] ignored requirements.txt line:', '`' + line + '`', '(not in pip-freeze)', file=sys.stderr)
                print(line)
        else:
            print('[warning] ignored requirements.txt line:', '`' + line + '`', '(not formatted as "pkg==version")', file=sys.stderr)
            print(line)


def unpinmyreqs():
    if len(sys.argv) != 2 or not sys.stdin.isatty():
        print('usage: unpinmyreqs requirements.txt', file=sys.stderr)
        return -1

    for line in open(sys.argv[1]):
        line = line.strip()
        m = re.match(RE_PKG, line)
        if m:
            print(m.group(1))
        else:
            print(line)
