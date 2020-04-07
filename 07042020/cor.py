"""Solution"""

import sys
from math import sqrt


def run():
    """Main func"""
    a_coef = int(sys.argv[1])
    b_coef = int(sys.argv[2])
    c_coef = int(sys.argv[3])
    diskr = b_coef * b_coef - 4 * a_coef * c_coef
    if diskr >= 0:
        t1_coef = (-b_coef + sqrt(diskr)) / (2 * a_coef)
        t2_coef = (-b_coef - sqrt(diskr)) / (2 * a_coef)
        res_eq = set()
        if t1_coef >= 0:
            res_eq.add(sqrt(t1_coef))
            res_eq.add(-sqrt(t1_coef))
        if t2_coef >= 0:
            res_eq.add(sqrt(t2_coef))
            res_eq.add(-sqrt(t2_coef))
        if len(res_eq) != 0:
            print("{} solutions: ".format(len(res_eq)), *res_eq)
        else:
            print("No solutions")
    else:
        print("No solutions")

run()
