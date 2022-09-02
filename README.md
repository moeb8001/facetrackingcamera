# **Face tracking camera**
Personal project (Open Hardware Academy 2022)
## **Introduction**
### Description of the project
In simple words, this device is a recording device which tracks the face of the person in front of it and in case of any movement it follows the face (in order to make sure that the face of the person being recorded is always in the centre of the screen). The main components of this device are a Raspberry pi 4 (the brain of the device) and a pi camera (responsible for capturing footage). In addition to the Raspberry pi and the pi camer, his device consists of 2 servo motors which enable the camera to rotate in 2 different axis. The rotating servo mptors allow the camera to have a wider view compared to a stationary camer, allowing it to follow the face as it moves.

### Programming languages and libraries used
For this project the programming language ``` Python ``` along with the ```Python OpenCV library``` were used. OpenCV is one of the most used python libraries for computer vision applications.  

### Overview of materials used:
1. Raspberry pi 4 x1
1. Pi camera (V1.3) x1
1. Servo motors x2

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
