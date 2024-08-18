# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:03:43 2024

@author: Ha
"""
import math
print("Giải phương trình bậc hai: ax^2+bx+c")
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
c = float(input("Nhập hệ số c:"))
if a==0:
    if b==0:
        if c==0:
            print("PT vô số nghiệm.")
        else:
            print("PT vô nghiệm.")
    else:
            if c==0:
                print("PT có 1 nghiệm x=0.")
            else:
                x= -c/b
                print("PT có 1 nghiệm: ",x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        x = (-b/(2*a))
        print("PT có nghiệm kép. x1 = x2 = ",x)
    else:
        print("PT có 2 nghiệm phân biệt")
        x1 = (-b + math.sqrt(delta)/(2*a))
        x2 = (-b - math.sqrt(delta)/(2*a))
        print("x2: ",x2)
        