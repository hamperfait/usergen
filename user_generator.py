#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:43:52 2017

@author: hamperfait
"""

import argparse
import os.path
import string
import sys
import subprocess

# Name part
parser = argparse.ArgumentParser(description='Generate usernames with A LOT of different of options.')
parser.add_argument("-n", "--Names", help="The path to the file containing the dictionary with names. If no path is specified, initials will be used.", default="")
parser.add_argument("-mN", "--min-chars-N", help="The minimum number of chars from the Name. Default is 1.", type=int, default=1)
parser.add_argument("-xN", "--max-chars-N", help="The maximum number of chars from the Name. Default is 1.", type=int, default=7)

# Surname part
parser.add_argument("Surnames", help="The path to the file containing the dictionary with names.")
parser.add_argument("-mS", "--min-chars-S", help="The minimum number of chars from the Surname.", type=int, default=1)
parser.add_argument("-xS", "--max-chars-S", help="The maximum number of chars from the Surname.", type=int, default=7)

#Year part
parser.add_argument("-y", "--year", help="Add a year (or more) at the end", type=int, nargs='+')
parser.add_argument("-yr", "--year-range", help="Add a range of years that are to be added at the end", type=int, nargs=2)
parser.add_argument("-d", "--digits", help="The number of digits that will be addded (1990 vs 90). Can also be used to add numbers from 0 to 9.", type=int, nargs='+', choices=[0,1,2,3,4], default=[0])

# Misc
parser.add_argument("-u", "--union", help="Select if you want a binding character [_ . - ] etc. Default is None. ", nargs='+', default=[""])
parser.add_argument("-o", "--output", help="If you want to specify the name of the output file. Default is... usernames!Yay!", default="usernames!Yay!.txt")
parser.add_argument("-m", "--mode", help="If you want the results to be appended to the file or to overwrite. Default is overWrite.", choices=["a", "w"], default="w")
parser.add_argument("--order", help="Choose wheter name goes first or second", type=int, choices=[1,2])
parser.add_argument("-dX", "--delete-duplicates", help="Delete the duplicates in the file")

results = parser.parse_args()
print(results)

def check_files():
    if results.Names and not os.path.isfile(results.Names):
        print("We're sorry. We didn't find the file in the specified directory. And we're NOT going to generate it for you ;)")
        sys.exit()
    if not results.Surnames is not None and os.path.isfile(results.Surnames):
        print("We're sorry. Didn't we say the Surnames file actually must exist? We might have forgotten, sorry...")
        sys.exit()

def delete_duplicates():
    lines_seen = set() # holds lines already seen
    with open("uniq_names", "w") as outfile:
        with open(results.output, "r") as reader:
            for line in reader:
                if line not in lines_seen: # not a duplicate
                    outfile.write(line)
                    lines_seen.add(line)
    
def main():
    with open(results.output, results.mode.lower()) as usernames:
        try:
            names = open(results.Names, 'r')
        except IOError:
            print("We can only work with initials, not a file!")
            names=list(string.ascii_lowercase)
            pass
        for name in names:
            with open(results.Surnames, 'r') as surnames:
                for surname in surnames:
                    for namechars in range(results.min_chars_N, results.max_chars_N+1):
                        for surnamechars in range(results.min_chars_S, results.max_chars_S+1):
                            for union in results.union:
                                for digits in results.digits:
                                    if results.year_range is not None:
                                        for year in range(results.year_range[0], results.year_range[1]):
                                            usernames.write("%s%s%s%d\n" % (name[:min(len(name), namechars)].lower(), union, surname[:min(len(surname), surnamechars)].lower(), year))
                                    elif results.year is not None:
                                        for year in results.year:
                                            usernames.write("%s%s%s%d\n" % (name[:min(len(name), namechars)].lower(), union, surname[:min(len(surname), surnamechars)].lower(), year))
                                    else:
                                        usernames.write("%s%s%s\n" % (name[:min(len(name), namechars)].lower(), union, surname[:min(len(surname), surnamechars)].lower()))
if __name__ == "__main__":
    check_files()
    main()
    if results.delete_duplicates:
        if sys.platform == "linux" or sys.platform == "linux2":
            subprocess.call("sort %s | uniq > %s" % (results.output, "temp.txt"), shell = True)
            os.rename("temp.txt", results.output)
        else:
            delete_duplicates()