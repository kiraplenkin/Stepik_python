import sys
import re

pattern = r'\\'

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line):
        print(line)
