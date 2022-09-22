# **Face tracking camera**
Personal project (Open Hardware Academy 2022)
<!-- ## **Introduction** -->
 ### Description of the project  
This device is a recording device which is able to recognize any face in front of it. Furthermore, in case of any movement this camera set-up makes use of two servo motors to rotate horizantally and vertically in order to to make sure the face of the person being recorded is always in the centre of the screen. The main components of this device are a Raspberry pi 4 (the brain of the device) and a pi camera (responsible for capturing footage). In addition to the Raspberry pi and the pi camera, this device consists of 2 servo motors which enable the camera to rotate in 2 different axis. The rotating servo motors are the main elements allowing the camera to have a wider view compared to a stationary camer. It is this feature which allows it to follow the face as it moves.

### Inspiration
This project was partly inspired by the new Insta360 Link 4K webcam which become super popular because of its ability to rotate and follow faces. It is also able to rotate and record your desk. The main downside of this device is its price. This product comes at a price of 380$ - 400$, which is very unaffordable for most, and in my opinion no webcam is really worth this much money. This project aims at making an affordable, fully functional version of this camera. For the picture of the aformentioned device refer to the picture in the chapter "Overview of steps taken"

### Programming languages and libraries used
For this project the programming language ``` Python ``` along with the ```Python OpenCV library (Open Source Computer Vision Library)``` were used. OpenCV is one of the most used python libraries for computer vision applications. Furthermore, for face recognition  the ```Harcascade classifier``` was used. Harcascade is an open source Face recognition classifier which can be found on [Github](https://github.com/opencv/opencv/tree/master/data/haarcascades).



### Main Components:
1. Raspberry pi 4 x1
1. Pi camera (V1.3) x1
1. Servo motors x2

For a detailed bill of material refer to the [Bill_Of_Materials.xlsx](https://github.com/moeb8001/facetrackingcamera/blob/main/Bill_Of_Materials.xlsx) in the Repository.




### Overview of steps taken
First a rough idea of the mechanism whihc enabled the camera to rotate about 2 axis was sketched. The idea was inspired by normal gimbals used for cameras.
<!--- |![Initial sketch](https://i.imgur.com/MkXis10.jpg =300x200)|
|:--:| 
| Initial idea/sketch |

|![](https://i.imgur.com/l4NTfpp.jpg)|
|:--:| 
| The inspiration |--->


Initial idea/sketch             |  Inspiration (A. A camera gimabal B. The new 370$ insta 360 webcam)
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/112695184/191833284-2e627725-c3d1-44d6-a044-ef9256955328.png)  |  ![](https://i.imgur.com/l4NTfpp.jpg)
  [ empty ] | ![image](https://user-images.githubusercontent.com/112695184/191833070-161108ca-7df0-4cce-99eb-20ee3b9895b5.png)



Furthermore, a program needed to be coded using python and the OpenCV library in order for the device to be able to detect faces and follow the face and keep it in the center (using the rotating servo motors).

Finally the servo motors and the camera were measured (measurements were double checked using the internet). Using these measurements the mecahnism was designed using Solidworks. The design was saved as STL in order to be 3d printed.


(More clear explanations along with all the complete files will be added later when theyr are fuly done)
