# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:11:59 2024

@author: Ha
"""

import math
print("Kiểm tra xem là tam giác gì ?")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a == b == c:
    print("Tam giác đều.")
elif a**2 + b**2 == c**2:
    print("Tam giác vuông.")
elif a == b or b == c or a == c:
    print("Tam giác cân.")
else:
    print("Tam giác thường.")
    
    
    
        