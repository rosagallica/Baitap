# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:19:24 2024

@author: Ha
"""

GPA = float(input("Nhập điểm trung bình (GPA):"))
if GPA < 3.5:
    print("Học lực Kém.")
elif GPA >= 3.5 and GPA < 5.0:
    print("Học lực Yếu.")
elif GPA >= 5.0 and GPA < 7.0:
    print("Học lực Trung bình.")
elif GPA >= 7.0 and GPA < 8.0:
    print("Học lực Khá.")
elif GPA >= 8.0 and GPA < 9.0:
    print("Học lực Giỏi")
elif GPA >= 9.0 and GPA <= 10:
    print("Học lực Xuất sắc.")