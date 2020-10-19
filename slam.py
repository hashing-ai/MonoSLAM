#!/usr/local/bin/python3
import cv2 as ai
import numpy as np


import os


theta = 20
phi = 40
shi = 20

theta = np.deg2rad(theta)
phi = np.deg2rad(phi)
shi = np.deg2rad(shi)

print(f'Theta : {theta:.4f} \n  Phi : {phi:.4f} \n  Shi : {shi:.4f}')

x = theta/2
y = phi/2
z = shi/2

qx = np.cos(x)*(np.array([1,0,0,0])) + np.sin(x)*np.array([0,0,1,0])
qy = np.cos(y)*(np.array([1,0,0,0])) + np.sin(y)*np.array([0,1,0,0])
qz = np.cos(z)*(np.array([1,0,0,0])) + np.sin(z)*np.array([0,0,0,1])

print(qx)
print(qy)
print(qz)

q = ((qz.dot(qx).T).dot(qy)).T


print('Final Quaternion : ', q)
