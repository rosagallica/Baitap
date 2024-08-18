# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:23:24 2024

@author: Ha
"""

print("Tính tiền taxi theo số km quãng đường đi được.")
km = float(input("Nhập số quãng đường đã đi: "))
if km == 1:
    t = 20
    print("Tiền taxi là: ",t)
elif km > 1 and km < 3:
    t = 13*km
    print("Tiền taxi là: ",t)
elif km >= 4 and km <= 8:
    t = 3*13 + (km-3)*12
    print("Tiền taxi là: ",t)
else: 
    t = 39 + 60 + (km-8)*10
    p = t*0.92
    print("Tiền taxi sau khi giảm:",p)
    


