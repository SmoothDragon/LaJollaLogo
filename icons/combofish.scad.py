#!/usr/bin/env python

import solid as sd
import numpy as np
import sys

phi = (np.sqrt(5)+1)/2

def starfish(R, ratio=.20, pieces=5, iterations=3):
    scale = 1-1/phi
    wedge = sd.square(R)
    wedge = sd.intersection()(
                sd.rotate([0,0,18])(wedge),
                sd.rotate([0,0,72])(wedge),
                sd.translate([-R/2,0])(wedge),
                )
    wedge = sd.translate([0,-R])(wedge)
    wedge = sd.rotate([0,0,180])(wedge)
    base = sd.union()(*[sd.rotate([0,0,i*360/pieces])(wedge) for i in range(pieces)])
    for _ in range(iterations):
        base2 = sd.scale(scale)(base)
        base3 = sd.translate([0,(1-scale)*R])(base2)
        base += sd.union()(*[sd.rotate([0,0,i*360/pieces])(base3) for i in range(pieces)])
    return base

def snowfish(R, pieces=5, iterations=3):
    scale = (3-np.sqrt(5))/2
    shift = (np.sqrt(5)-1)/2
    base = sd.circle(R, segments=pieces)
    for _ in range(iterations):
        base2 = sd.scale(scale)(base)
        base3 = sd.translate([R*shift,0])(base2)
        base = sd.union()(*[sd.rotate([0,0,i*360/pieces])(base3) for i in range(pieces)])
        base += sd.rotate([0,0,180])(base2)
    base = sd.rotate([0,0,90])(base)
    return base

if __name__ == '__main__':
    fn = 512
    R = 100
    iterations = 2
    star = starfish(R,iterations=iterations)
    if TrueL
        scale = 2*np.sqrt(5)-4
        snow = snowfish(scale*R,iterations=iterations)
    else:
        scale = .35
        snow = snowfish(scale*R,iterations=iterations)
        snow = sd.rotate([0,0,180])(snow)
    total = star - snow
    print(sd.scad_render(total, file_header=f'$fn={fn};'))
