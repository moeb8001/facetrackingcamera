# **Face tracking camera**
Personal project (Open Hardware Academy 2022)
<!-- ## **Introduction** -->
 ### Description of the project  
This device is a recording device which is able to recognize any face in front of it. Furthermore, in case of any movement this camera set-up makes use of two servo motors to rotate horizantally and vertically in order to to make sure the face of the person being recorded is always in the centre of the screen. The main components of this device are a Raspberry pi 4 (the brain of the device) and a pi camera (responsible for capturing footage). In addition to the Raspberry pi and the pi camera, this device consists of 2 servo motors which enable the camera to rotate in 2 different axis. The rotating servo motors are the main elements allowing the camera to have a wider view compared to a stationary camer. It is this feature which allows it to follow the face as it moves.

### Programming languages and libraries used
For this project the programming language ``` Python ``` along with the ```Python OpenCV library (Open Source Computer Vision Library)``` were used. OpenCV is one of the most used python libraries for computer vision applications. Furthermore, for face recognition  the ```Harcascade classifier``` was used. Harcascade is an open source Face recognition classifier which can be found on [Github](https://github.com/opencv/opencv/tree/master/data/haarcascades).



### Main Components:
1. Raspberry pi 4 x1
1. Pi camera (V1.3) x1
1. Servo motors x2

For a detailed bill of material refer to forlde [Docs]()




### Overview of steps taken
First a rough idea of the mechanism whihc enabled the camera to rotate about 2 axis was sketched. The idea was inspired by normal gimbals used for cameras.
<!--- |![Initial sketch](https://i.imgur.com/MkXis10.jpg =300x200)|
|:--:| 
| Initial idea/sketch |

|![](https://i.imgur.com/l4NTfpp.jpg)|
|:--:| 
| The inspiration |--->


Initial idea/sketch             |  Inspiration
:-------------------------:|:-------------------------:
![](https://i.imgur.com/MkXis10.jpg =400x300)  |  ![](https://i.imgur.com/l4NTfpp.jpg)


Furthermore, a program needed to be coded using python and the OpenCV library in order for the device to be able to detect faces and follow the face and keep it in the center (using the rotating servo motors).

Finally the servo motors and the camera were measured (measurements were double checked using the internet). Using these measurements the mecahnism was designed using Solidworks. The design was saved as STL in order to be 3d printed.
