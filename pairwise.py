# coding=utf-8
from __future__ import print_function

import itertools

params = [
    ['sd', 'mic', 'geo', 'cam'],
    ['site', 'sys', 'protect'],
    ['on', 'off', 'on -> off: bro', 'on -> off: system'],
    ['same', 'new'],
    ['same', 'new'],
    ['same', 'new']
]

pairs = itertools.product(*params, repeat=1)

print("PAIRWISE:")
for i, pairs in enumerate(pairs):
    print("{:2d}: {}".format(i, pairs))