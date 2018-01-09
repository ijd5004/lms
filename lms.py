#!/usr/bin/env/python
"""
Module: lms
Engineer: Ian Davis
Date: January 9, 2018
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
    nsets = len(data)   #number of points in data
    inp_x = np.empty(nsets)
    inp_y = np.empty(nsets)
    print '\n'
    print 'Overdetermined linear system:'
    for i in range(nsets):
        inp_x[i] = data[i][0]
        inp_y[i] = data[i][1]
        print 'beta1 +',inp_x[i],'* beta2 = ',inp_y[i]

    #(Test 3) Display the "sum of the squares" function
    #General form of the equation:
    # S(beta1,beta2) =  y^2             (term1)
    #                 + beta1^2         (term2)
    #                 + x^2*beta2^2     (term3)
    #                 - 2*y*beta1       (term4)
    #                 - 2*y*x*beta2     (term5)
    #                 + 2*x*beta1*beta2 (term6)
    terms = np.array([0.0,0.0,0.0,0.0,0.0,0.0])
    for i in range(nsets):
        terms[0] = terms[0] + inp_y[i]*inp_y[i]
        terms[1] = terms[1] + 1.0
        terms[2] = terms[2] + inp_x[i]*inp_x[i]
        terms[3] = terms[3] - 2.0*inp_y[i]
        terms[4] = terms[4] - 2.0*inp_y[i]*inp_x[i]
        terms[5] = terms[5] + 2.0*inp_x[i]
    print '\n'
    print 'Sum of the squares:'
    print 'S(beta1,beta2) = '+str(terms[0])+' + ' \
                            +str(terms[1])+'*beta1^2 + ' \
                            +str(terms[2])+'*beta2^2 + ' \
                            +str(terms[3])+'*beta1 + ' \
                            +str(terms[4])+'*beta2 + ' \
                            +str(terms[5])+'*beta1*beta2'

    #(Test 4) Display the partial derivative equations for the coeff.
    # dS/dbeta1 = 2*beta1 - 2*y + 2*x*beta2 = 0
    #             (2*terms[1])*beta1 + terms[3] + terms[5]*beta2 = 0
    # dS/dbeta2 = 2*x^2*beta2 - 2*y*x + 2*x*beta1 = 0
    #             2*terms[2]*beta2 + terms[4] + terms[5]*beta1 = 0

    print '\n'
    print 'Partial derivatives:'
    print 'dS/dbeta1 = '+str(2*terms[1])+'*beta1 + '+str(terms[3])+' + '+str(terms[5])+'*beta2'
    print '\n'
    print 'dS/dbeta2 = '+str(2*terms[2])+'*beta2 + '+str(terms[4])+' + '+str(terms[5])+'*beta1'
    
    #(Test 5) Display the solution
    # dS/dbeta1 = 2*beta1 - 2*y + 2*x*beta2 = 0
    #             (2*terms[1])*beta1 + terms[3] + terms[5]*beta2 = 0
    #             beta1 = -terms[3]/(2*terms[1]) - terms[5]/(2*terms[1])*beta2
    # dS/dbeta2 = 2*x^2*beta2 - 2*y*x + 2*x*beta1 = 0
    #             (2*terms[2])*beta2 + terms[4] + terms[5]*beta1 = 0
    #             (2*terms[2])*beta2 + terms[4] + terms[5]*(-terms[3]/(2*terms[1]) - terms[5]/(2*terms[1])*beta2) = 0
    #             (2*terms[2])*beta2 + terms[4] - terms[5]*terms[3]/(2*terms[1])- terms[5]*terms[5]/(2*terms[1])*beta2 = 0
    #             beta2*(2*terms[2] - terms[5]*terms[5]/(2*terms[1])) = terms[5]*terms[3]/(2*terms[1]) - terms[4]
    #             beta2 = (terms[5]*terms[3]/(2*terms[1]) - terms[4])/(2*terms[2] - terms[5]*terms[5]/(2*terms[1]))
    beta2 = (terms[5]*terms[3]/(2*terms[1]) - terms[4])/(2*terms[2] - terms[5]*terms[5]/(2*terms[1]))
    beta1 = -terms[3]/(2*terms[1]) - terms[5]/(2*terms[1])*beta2
    print '\n'
    print 'Solution:'
    print 'beta1 = '+str(beta1)
    print 'beta2 = '+str(beta2)
    print 'y = '+str(beta2)+'*x + '+str(beta1)

    #(Test 6) Display the sum of squares of the residuals
    Sres = 0.0
    for i in range(nsets):
        Sres = Sres + (inp_y[i] - (beta1 + inp_x[i]*beta2))**2
    print '\n'
    print 'Sum of squares of the residuals: '+str(Sres)
