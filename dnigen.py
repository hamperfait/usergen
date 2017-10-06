#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:52:18 2017

@author: hamperfait
"""

import argparse
import os.path
import sys

parser = argparse.ArgumentParser(description='Generate spanish DNIs with some options.')
parser.add_argument("-a", "--amount", help="The number of IDs to generate. Default is 100.", type=int, default=100)
parser.add_argument("-s", "--start", help="The number at which the generator has to start.", type=int, default=40000000)
parser.add_argument("-e", "--end", help="The maximum number of chars from the Name. Default is 1.", type=int)
parser.add_argument("-l", "--letter", help="Specify numbers only finishing with the specified letters", nargs='+', choices=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E'])
parser.add_argument("-st", "--steps", help="Specify the steps between ID numbers.", type=int, default=1)
parser.add_argument("-o", "--output", help="Specify the output. Default is... DNIs!Yay!", default="DNIs!Yay!")
parser.add_argument("-m", "--mode", help="Whether you want to Append or to overWrite", choices=["a","w"], default="w")


results = parser.parse_args()
print(results)

def check_input(start, end):
    if end < start:
        print("You lil' rebel! Tryin' to mess with me?")
        return end, start
    else:
        return start, end
    
def dnigen(start, end):
    with open(results.output, results.mode) as writer:
        for dni in range(start, end, results.steps):
            mod = dni % 23
            if mod == 0:
                letter='T'
            elif mod == 1:
                letter='R'
            elif mod == 2:
                letter='W'
            elif mod == 3:
                letter='A'
            elif mod == 4:
                letter='G'
            elif mod == 5:
                letter='M'
            elif mod == 6:
                letter='Y'
            elif mod == 7:
                letter='F'
            elif mod == 8:
                letter='P'
            elif mod == 9:
                letter='D'
            elif mod == 10:
                letter='X'
            elif mod == 11:
                letter='B'
            elif mod == 12:
                letter='N'
            elif mod == 13:
                letter='J'
            elif mod == 14:
                letter='Z'
            elif mod == 15:
                letter='S'
            elif mod == 16:
                letter='Q'
            elif mod == 17:
                letter='V'
            elif mod == 18:
                letter='H'
            elif mod == 19:
                letter='L'
            elif mod == 20:
                letter='C'
            elif mod == 21:
                letter='K'
            elif mod == 22:
                letter='E'
            if results.letter is None:
                writer.write('%08d%s\n' % (dni, letter))
            else:
                if letter in results.letter:
                    writer.write('%08d%s\n' % (dni, letter))


if __name__ == "__main__":
    if results.end is not None:
        start, end = check_input(results.start, results.end)
    else:
        start =results.start
        end = results.start + results.amount
    dnigen(start, end)