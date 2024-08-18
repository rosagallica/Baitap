# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:55:17 2024

@author: Ha
"""
print("Giải phương trình bậc nhất: ax+b=0")
a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else: 
    x = -b/a
    print("Nghiệm của phương trình là:", -b/a)