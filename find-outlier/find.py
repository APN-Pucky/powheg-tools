#!/usr/bin/python

import pylhe
import sys
import numpy as np

abs_max=[]

rel_max=[]

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
            abs_max.append( ( max_difference,i,arg))
        if rel_difference > v_rel_max:
            rel_max.append( ( max_difference,i,arg))
            rel_max = rel_difference
        #print(i,max_difference)
    #print(pylhe.read_lhe_init(arg))
print(sys.argv[1:])
print(v_abs_max, i_abs_max, f_abs_max)
print(v_rel_max, i_rel_max, f_rel_max)

