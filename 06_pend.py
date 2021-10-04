#!/usr/bin/ python3
# -*- coding: utf-8 -*-

''' 
Solution to pendulum exercise:
    \dot{x} = y
    \dot{y} = -\sin x
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.integrate import odeint

def rhs_pend (y, t):
    """ RHS equations for the pendulum system """
    # Unpack both coordinates
    X, Y = y
    # Derivatives
    dydt = [
            Y,
            np.sin(X)
    ]
    return dydt

def integrate (y0, t, rhs_fun):
    """ Given an initial condition x0 and a time vector structure, integrates
    the system described by rhs_fun(y, t)i. Returns the solution array """
    sol, info = odeint(rhs_fun, y0, t, full_output = True)
    return sol

# Define a set of initial conditions
tp = np.linspace(0, 5, 50)
tn = np.linspace(0, -5, 50)
X, Y = np.meshgrid(np.linspace(-8, 8, 9), np.linspace(-3, 3, 9))
plt.figure()
for y0 in zip(X.ravel(), Y.ravel()):
    solp = integrate(y0, tp, rhs_pend)
    soln = integrate(y0, tn, rhs_pend)
    plt.plot(solp[:, 0], solp[:, 1], 'k--')
    plt.plot(soln[:, 0], soln[:, 1], 'k--')
plt.xlim([-8,8])
plt.ylim([-3,3])
plt.show()
