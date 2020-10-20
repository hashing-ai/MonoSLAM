# SLAM

## What is SLAM ?
- stands for "simultaneous localization and mapping""

Currently, there are many ways to do SLAM with monocular camera.
But, let's start from  [MonoSLAM : A Real-Time Single Camera SLAM](https://www.doc.ic.ac.uk/~ajd/Publications/davison_etal_pami2007.pdf)


## SLAM Based on IMU and Monocular

<p align='justify'>
We have to integrate the data coming from IMU and monocular camera. Let's first take a look at some conversion relations among various co-ordinate systems and then we will dive into obtaining the pose through IMU data and standalone monocular SLAM. And finally, we will fuse these data to get the final pose of the vehicle.
</p>

## Co-ordinate Coversion

<p align='justify'>
The co-ordinates involved in this system would be the global, vehicle, camera and IMU. The center of the vehicle at the initial position is set as the origin of the global co-ordinate system and the vehicle's vertical axis is set as the x-axis of the global co-ordinate, the horizontal axis is set as the y-axis.

The data obtained from each sesor is based on its own co-ordinate system, so the first task is for merging mutliple sensor data is transformation of the co-ordinate system.

All the co-ordinate systems are uniformly transformed into a global reference frame. The Euler angles between the vehicle/camera and the global co-ordinate system are measured from VSLAM (rotation matrix). The Eular angles of the IMU can be calculated from the sensor.
</p>

## IMU Pose Estimation

### Orientation :
IMU orientation estimation is based on the angular velocity, which is measured by the tri-axial gyroscope. 

:: steps ::
- Calculate static quaternion by the factored quaternion algorithm
- Estimate the dynamic quaternion by the differential relation between the angular velocity and the quaternion
- Merge the static quaternion with dynamic quaternion together by Kalman Filter
- Achieve pose estimation

<p align='justify'> 
In general, there must be filter processing due to the gyro drift and measurement noise. 
The quaternion is set as state vector `x = q`. 


