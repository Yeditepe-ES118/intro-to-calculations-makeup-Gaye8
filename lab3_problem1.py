#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 20:04:06 2025

@author: gayeakyuz
"""

import numpy as np
def triangle(x,y):
    theta = np.arctan(x/y) * 180/np.pi #in degrees
    gamma = np.arctan(y/x) * 180/np.pi #in degrees
    d = np.sqrt(x**2 + y**2)
    s = 1/np.cos(theta*np.pi/180)
    return theta, gamma, d, s 
myresult = triangle(3,4)

            