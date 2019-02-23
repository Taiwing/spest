#!/usr/bin/python

import os
import sys
import time

if len(sys.argv) < 3:
    sys.exit()

command = sys.argv[1]
n = int(sys.argv[2])

i = 0
start = 0
end = 0
times = []
while i < n:
    start = time.time()
    os.popen(command + " &> /dev/null")
    end = time.time()
    times.append(end - start)
    i += 1
print("times:")
print(times)
print("\naverage:")
print(sum(times)/n)

