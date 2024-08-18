# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:09:54 2024

@author: Ha
"""

from random import randint
player = int(input("Bạn vui lòng chọn: 1. Kéo, 2. Búa, 3. Bao: "))
computer = randint(1, 3)
if computer == 1:
    print("Máy chọn kéo")
if computer == 2:
    print("Máy chọn búa")
if computer == 3:
    print("Máy chọn bao")
if computer == player:
    print("Player và Computer Hòa")
if computer == 1 and player == 2:
    print("Bạn Thắng")
if computer == 1 and player == 3:
    print("Bạn thua")
if computer == 2 and player == 1:
    print("Bạn thua")
if computer == 2 and player == 3:
    print("Bạn thắng")
if computer == 3 and player == 1:
    print("Bạn thắng")
if computer == 3 and player == 2:
    print("Bạn thua")

