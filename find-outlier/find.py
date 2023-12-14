#!/usr/bin/python

import pylhe
import sys
import numpy as np

v_abs_max=0
i_abs_max = 0
f_abs_max = ""

v_rel_max=0
i_rel_max=0
f_rel_max=""

for arg in sys.argv[1:]:
    for i,event in enumerate(pylhe.read_lhe_with_attributes(arg)):
        #print(event.particles)
        #print(event.weights)
        warr = np.array(list(event.weights.values()))
        warr = warr[7:]
        #print(warr)
        max_difference = np.max(np.abs(np.subtract.outer(warr, warr)))
        # relative difference
        rel_difference = max_difference / np.average(warr)

        if max_difference > v_abs_max:
            v_abs_max = max_difference
            i_abs_max = i
            f_abs_max = arg
        if rel_difference > v_rel_max:
            v_rel_max = rel_difference
            i_rel_max = i
            f_rel_max = arg
        #print(i,max_difference)
    #print(pylhe.read_lhe_init(arg))
print(sys.argv[1:])
print(v_abs_max, i_abs_max, f_abs_max)
print(v_rel_max, i_rel_max, f_rel_max)

