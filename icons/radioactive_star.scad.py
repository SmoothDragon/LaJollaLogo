#!/usr/bin/env python

import solid as sd


def symbol(R, ratio=.20, pieces=5):
    inner = ratio * R
    gap = R/20
    base = sd.circle(R-2*gap)
    cutter = sd.square(2*R)
    cutter = sd.intersection()(
                cutter,
                sd.rotate([0,0,180/pieces-90])(cutter),
                # sd.rotate([0,0,360/pieces-90])(cutter),
                )
    base = sd.intersection()(base, cutter)
    base = sd.union()(*[sd.rotate([0,0,i*360/pieces])(base) for i in range(pieces)])
    base -= sd.circle(inner + gap)
    base += sd.circle(inner)
    outer = sd.circle(R)
    outer -= sd.circle(R-gap)
    return base, outer

if __name__ == '__main__':
    fn = 512
    R = 100
    base, outer = symbol(R)
    # total = sd.translate([R,R])(total)
    # print(sd.scad_render(total, file_header=f'$fn={fn};'))
    print(sd.scad_render(outer, file_header=f'$fn={fn};'))
    print(sd.scad_render(base, file_header=f'$fn={fn};'))
