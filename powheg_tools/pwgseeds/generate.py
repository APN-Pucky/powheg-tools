#!/usr/bin/env python3

n = 2000
start = 4
end = 32768
with open("pwgseeds.dat", "w") as f:
    for i in range(start, end, int(end / n)):
        print(i, file=f)
