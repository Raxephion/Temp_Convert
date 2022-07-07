# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 19:08:50 2022

@author: Pierre-Henri Rossouw

60 Apps in 60 Days Challenge - App #12: Temperature Coverter


"""


def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

print(convert(78))