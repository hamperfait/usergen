#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:43:52 2017

@author: hamperfait
"""

import argparse
import os.path
import sys
# Name part
parser = argparse.ArgumentParser(description='Generate usernames with A LOT of different of options.')
parser.add_argument("Names", help="The path to the file containing the dictionary with names.")
parser.add_argument("-mN", "--min-chars-N", help="The minimum number of chars from the Name. Default is 1.", type=int, default=1)
parser.add_argument("-xN", "--max-chars-N", help="The maximum number of chars from the Name. Default is 1.", type=int, default=1)

# Surname part
parser.add_argument("Surnames", help="The path to the file containing the dictionary with names.")
parser.add_argument("-mS", "--min-chars-S", help="The minimum number of chars from the Surname. Default is 7.", type=int, default=7)
parser.add_argument("-xS", "--max-chars-S", help="The maximum number of chars from the Surname. Default is 7.", type=int, default=7)

# Misc
parser.add_argument("-u", "--union", help="Select if you want a binding character [_ . - ] etc. Default is None. ", nargs='+', default=[""])
parser.add_argument("-o", "--output", help="If you want to specify the name of the output file. Default is... usernames! Yay!", default="usernames! Yay!.txt")
parser.add_argument("-m", "--mode", help="If you want the results to be appended to the file or to overwrite. Default is overWrite.", choices=["a", "w"], default="w")
results = parser.parse_args()
print(results)

if not os.path.isfile(results.Names):
    print("We're sorry. Didn't we say the Names file actually must exist? We might have forgotten, sorry...")
    sys.exit()
if not os.path.isfile(results.Surnames):
    print("We're sorry. Didn't we say the Surnames file actually must exist? We might have forgotten, sorry...")
    sys.exit()

with open(results.output, results.mode.lower()) as usernames:
    with open(results.Names, 'r') as names:
        for name in names:
            with open(results.Surnames, 'r') as surnames:
                for surname in surnames:
                    for namechars in range(results.min_chars_N, results.max_chars_N+1):
                        for surnamechars in range(results.min_chars_S, results.max_chars_S+1):
                            for union in results.union:
                                usernames.write("%s%s%s\n" % (name[:namechars].lower(), union, surname[:surnamechars].lower()))