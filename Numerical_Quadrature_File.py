import numpy as np
from math import *


def f(x):
    return pi**2 * sin(pi*x)


def Numerical_Quadrature(e, i, quad_type, h):
    '''
    Calculate the numerical integration defined by eqns 14 and 15
    `e` element number
    `i` 1st or 2nd node within element
    `quad_type` 1 = Trapezium, 2 = Simpson's
    `h` = 1/Ne
    '''
    x_i = h*(e+i-1)
    if quad_type == 1: # Trapezium
        return (h/2) * f(x_i)
    elif quad_type == 2: # Simpson's
        return (h/2) * f(x_i) # TODO

