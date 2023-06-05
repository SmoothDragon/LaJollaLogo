#!/usr/bin/env python

import solid as sd
import numpy as np
import sys

phi = (np.sqrt(5)+1)/2

def symbol(R, pieces=5):
    scale = (3-np.sqrt(5))/2
    shift = (np.sqrt(5)-1)/2
    base = sd.circle(R, segments=pieces)
    for _ in range(3):
        base2 = sd.scale(scale)(base)
        base3 = sd.translate([R*shift,0])(base2)
        base = sd.union()(*[sd.rotate([0,0,i*360/pieces])(base3) for i in range(pieces)])
        base += sd.rotate([0,0,180])(base2)
    base = sd.rotate([0,0,90])(base)
    return base

def dragon(R):
    wing = sd.circle(R)
    wing = sd.intersection()(wing, sd.translate([R,0,0])(sd.square(2*R, center=True)))
    r_winghole = R/2.2
    winghole = sd.circle(r_winghole)
    r_winghook = r_winghole
    winghookhole = sd.circle(r_winghook)
    winghookhole = sd.translate([0,-r_winghook,0])(winghookhole)
    winghookhole = sd.rotate([0,0,-10])(winghookhole)
    winghookhole = sd.translate([0,R,0])(winghookhole)
    winghook = wing - winghookhole
    winghook = sd.intersection()(
        sd.translate([0,R-r_winghole,0])(winghole),
        winghook,
        )

    wing -= sd.translate([0,R-r_winghole,0])(winghole)
    wing -= sd.translate([0,-(R-r_winghole),0])(winghole)
    wing += winghook
    return wing 

def wing(R):
    block = sd.circle(R)
    wingback_ratio = .96
    r_wingback = R*wingback_ratio
    block -= sd.translate([-R*5*(1-wingback_ratio),0,0])(sd.circle(r_wingback))
    return block


if __name__ == '__main__':
    fn = 512
    R = 100
    total = dragon(R)
    total = wing(R)
    print(sd.scad_render(total, file_header=f'$fn={fn};'))
