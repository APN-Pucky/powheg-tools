import sys

import yoda

pdf = 99208082
numMembers = 39
# pdf=27100
# numMembers=65
start = 8
end = numMembers + start - 2
weights = {}
weights[1] = pdf
for i in range(start, end + 1):
    weights[i] = i + pdf - start + 1

for f in sys.argv[1:]:
    map = yoda.read(f)
    nmap = {}

    for k, v in map.items():
        n = k
        h = v
        nmap[k] = v
        for w, p in weights.items():
            n = n.replace(f"[W{w}]", f"[PDF{p}]")
            h.setPath(h.path().replace(f"[W{w}]", f"[PDF{p}]"))
        nmap[n] = h

    yoda.write(nmap, "pdf_" + f)
