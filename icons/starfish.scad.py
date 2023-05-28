#!/usr/bin/env python

import solid as sd
import numpy as np
import sys

phi = (np.sqrt(5)+1)/2

def symbol(R, pieces=5):
    scale = 1-1/phi
    base = sd.square(R)
    base = sd.intersection()(
                sd.rotate([0,0,18])(base),
                sd.rotate([0,0,72])(base),
                sd.translate([-R/2,0])(base),
                # sd.rotate([0,0,360/pieces-90])(cutter),
                )
    base = sd.translate([0,-R])(base)
    base = sd.rotate([0,0,180])(base)
    base = sd.union()(*[sd.rotate([0,0,i*360/pieces])(base) for i in range(pieces)])
    for _ in range(4):
        base2 = sd.scale(scale)(base)
        base2 = sd.translate([0,(1-scale)*R])(base2)
        base += sd.union()(*[sd.rotate([0,0,i*360/pieces])(base2) for i in range(pieces)])

    return base
    base = sd.union()(*[sd.rotate([0,0,i*360/pieces])(base) for i in range(pieces)])
    base2 = sd.scale(scale)(base)
    base2 = sd.translate([0,(1-scale)*R])(base2)
    base += sd.union()(*[sd.rotate([0,0,i*360/pieces])(base2) for i in range(pieces)])
    base3 = sd.scale(scale)(base)
    base3 = sd.translate([0,(1-scale)*R])(base3)
    base += sd.union()(*[sd.rotate([0,0,i*360/pieces])(base3) for i in range(pieces)])
    base3 = sd.scale(scale)(base)
    base3 = sd.translate([0,(1-scale)*R])(base3)
    base += sd.union()(*[sd.rotate([0,0,i*360/pieces])(base3) for i in range(pieces)])
    return base

if __name__ == '__main__':
    fn = 512
    R = 100
    total = symbol(R)
    print(sd.scad_render(total, file_header=f'$fn={fn};'))
