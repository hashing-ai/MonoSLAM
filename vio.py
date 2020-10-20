#!/usr/local/bin/python3
import cv2 as ai
import numpy as np


import os


theta = 10
phi = 20
shi = 40

theta = np.deg2rad(theta)
phi = np.deg2rad(phi)
shi = np.deg2rad(shi)

print(f'Theta : {theta:.4f} \n  Phi : {phi:.4f} \n  Shi : {shi:.4f}')

x = theta/2
y = phi/2
z = shi/2

cx = np.cos(x)
cy = np.cos(y)
cz = np.cos(z)
sx = np.sin(x)
sy = np.sin(y)
sz = np.sin(z)

class Quat():
    pass

qx = np.cos(x)*(np.array([1,0,0,0])) + np.sin(x)*np.array([0,0,1,0])
qy = np.cos(y)*(np.array([1,0,0,0])) + np.sin(y)*np.array([0,1,0,0])
qz = np.cos(z)*(np.array([1,0,0,0])) + np.sin(z)*np.array([0,0,0,1])

print(qx)
print(qy)
print(qz)

q = Quat()
q.w = cy * cx * cz + sy * sx * sz
q.x = sy * cx * cz - cy * sx * sz
q.y = cy * sx * cz + sy * cx * sz
q.z = cy * cx * sz - sy * sx * cz

q = np.array([q.x, q.y, q.z, q.w])
print('Final Quaternion :\n', q)

# the final Quaternion is equivalent to the the code below :
# scipy expects two things :
# - seq : ZYX (extrinsic)
# - euler angles: (shi, theta, phi)

# from scipy.spatial.transform import Rotation as R
# r = R.from_euler('ZYX',[shi, theta, phi ])
# xx = r.as_quat()
# print(xx)



