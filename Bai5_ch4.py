# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:55:24 2024

@author: Ha
"""

import math
print("Nhập 3 số a,b,c xem có phải 3 cạnh của tam giác không? ")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    print("a,b,c là 3 cạnh của tam giác.")
else:
    print("a,b,c không phải là 3 cạnh của tam giác.")