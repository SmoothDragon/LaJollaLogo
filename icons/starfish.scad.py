#!/usr/bin/env python

import solid as sd
import numpy as np
import sys

phi = (np.sqrt(5)+1)/2

def symbol(R, ratio=.20, pieces=5):
    inner = ratio * R
    gap = R/20
    scale = .5*(1 - np.sin(np.pi/10)/2)
    scale = 1-1/phi
    print(scale, file=sys.stderr)
    print(np.sin(np.pi/5)/1.6, file=sys.stderr)
    print(1-1/phi, file=sys.stderr)
    wedge = sd.square(R)
    wedge = sd.intersection()(
                sd.rotate([0,0,18])(wedge),
                sd.rotate([0,0,72])(wedge),
                sd.translate([-R/2,0])(wedge),
                # sd.rotate([0,0,360/pieces-90])(cutter),
                )
    wedge = sd.translate([0,-R])(wedge)
    wedge = sd.rotate([0,0,180])(wedge)
    base = sd.union()(*[sd.rotate([0,0,i*360/pieces])(wedge) for i in range(pieces)])
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
