#!/usr/bin/env/python
"""
Module: lms
Engineer: Ian Davis
Date: January, 7, 2018
Revision History:
The purpose of this module is to perform a linear regression
using the least mean square method.

The program will take an array of (x,y) points as an argument.
The program will determine the y-intercept and x-coefficient
for a linear regression model
"""

import numpy as np

def lms(data):

    #(Test 1) Check data is in the appropriate form
    try:
        data = np.array(data)
        print 'x:\ty:'
        for i in range(len(data)):
            print data[i][0], '\t', data[i][1]
    except:
        print 'Incorrect format!'
        return

    #(Test 2) Display the overdetermined linear system
    #General form equation: beta1 + x_i*beta2 = y_i
    inp_x = np.empty(len(data))
    inp_y = np.empty(len(data))
    print '\n'
    print 'overdetermined linear system:'
    for i in range(len(data)):
        inp_x[i] = data[i][0]
        inp_y[i] = data[i][1]
        print 'beta1 +',inp_x[i],'* beta2 = ',inp_y[i]

    #(Test 3) Display the "sum of the squares" function


    #(Test 4) Display the partial derivative equations for the coeff.


    #(Test 5) Display the solution


    #(Test 6) Display the sum of squares of the residuals