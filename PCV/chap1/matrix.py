# -*- coding: utf-8 -*-
__author__ = 'Natsutani'
# nupuを使った行列演算

import numpy as np

a = np.array([[ 1.0, -2.0, 3.0], [4.0, 5.0, 6.0], [-7.0, 8.0, -9.0]])
b = np.array([[10.0, -9.0, 8.0], [7.0, 6.0, 4.0], [-3.0, 2.0, -1.0]])

print("A + B")
print(a + b)

print("A - B")
print(a - b)

print("A * B (要素同士の積)")
print(a * b)

print("Aの逆行列")
print(np.linalg.inv(a))

print("A ・ B")
print(np.dot(a, b))

print("det A")
print(np.linalg.det(a))

print("転置 A")
print(np.transpose(a))

print("A + 5")
print(a + 5)

print("Aの5倍")
print(a * 5)

# 3次元ベクトルの内積・外積
c = np.array([ 1.0, -2.0, 3.0],)
d = np.array([ 4.0, -5.0, 6.0],)

print("C・D")
print(np.dot(c, d))

print("C×D")
print(np.cross(c, d))
