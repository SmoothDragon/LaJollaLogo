#!/usr/bin/env python

import svgpathtools as svg

paths, attributes = svg.svg2paths('ljtree.svg')

min_x = 1e10
min_y = 1e10
max_x = -1e10
max_y = -1e10

for path in paths:
    for seg in path:
        xy = seg.point(0)
        min_x = min(min_x, xy.real)
        min_y = min(min_y, xy.imag)
        max_x = max(max_x, xy.real)
        max_y = max(max_y, xy.imag)
print((min_x,min_y))
print((max_x,max_y))
shift_x = (max_x + min_x)/2
shift_y = (max_y + min_y)/2
shift = f'{shift_x+1j*shift_y}'[1:-1]
shift = f'{shift_x} {shift_y}'
print(shift)

output = svg.parser.parse_transform(f'translate({shift})')

