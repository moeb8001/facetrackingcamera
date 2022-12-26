# **Face tracking camera**
Personal project (Open Hardware Academy 2022)
<!-- ## **Introduction** -->
 ## Description of the project  
 
 
PiCamera is an open-source project that allows you to connect a Raspberry Pi camera to a Raspberry Pi and use servo motors to move the camera and track your face. This project was inspired by the Insta360 webcam and allows you to easily add facial tracking to your Raspberry Pi projects.

The idea of making such device was inspired by the new Insta360 webcam. The Insta360 webcam is a popular device that allows you to easily capture and share 360-degree video. It features a compact design and advanced technology that makes it easy to use, even for beginners. When I saw the Insta360 webcam, I was inspired to create a similar device using a Raspberry Pi and servo motors.

The code for PiCamera is written in Python and makes use of the OpenCV library and Haarcascade to detect and track faces. With just a few simple steps, you can get your PiCamera up and running and start tracking your face.

<!-- This device is a recording device which is able to recognize any face in front of it. Furthermore, in case of any movement this camera set-up makes use of two servo motors to rotate horizantally and vertically in order to to make sure the face of the person being recorded is always in the centre of the screen. The main components of this device are a Raspberry pi 4 (the brain of the device) and a pi camera (responsible for capturing footage). In addition to the Raspberry pi and the pi camera, this device consists of 2 servo motors which enable the camera to rotate in 2 different axis. The rotating servo motors are the main elements allowing the camera to have a wider view compared to a stationary camer. It is this feature which allows it to follow the face as it moves. -->

## Inspiration
This project was partly inspired by the new Insta360 Link 4K webcam which become super popular because of its ability to rotate and follow faces. The main downside of this device is its price. This product comes at a price of 380$ - 400$, which is very unaffordable for most. In my opinion no webcam is really worth this amount of money. This project aims at making an affordable, fully functional version of this camera. Below the intitial rough idea of the mechanism which enabled the camera to rotate about 2 axis was sketched by me can be seen. The idea was inspired by normal gimbals used for cameras. Additionally, the picture of Insta360 webcam, which was the main inspiration for this project can be seen on the right.
<!--- |![Initial sketch](https://i.imgur.com/MkXis10.jpg =x300)|
|:--:| 
| Initial idea/sketch |

|![](https://i.imgur.com/l4NTfpp.jpg =x100)|
|:--:| 
| The inspiration |--->


Initial idea/sketch           |  Inspiration
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/112695184/191833284-2e627725-c3d1-44d6-a044-ef9256955328.png" width="700" ><h4 align="center"> A. Sketch (own work)</h4> |<img src="https://i.imgur.com/l4NTfpp.jpg" width="350" >  <h4 align="center"> A. A camera gimabal </h4> <img src="https://user-images.githubusercontent.com/112695184/191833070-161108ca-7df0-4cce-99eb-20ee3b9895b5.png" width="350" > <h4 align="center">B. The new 370$ Insta360 webcam</h4>                                  

## Programming languages and libraries used
For this project the programming language ``` Python ``` along with the ```Python OpenCV library (Open Source Computer Vision Library)``` were used. OpenCV is one of the most used python libraries for computer vision applications. Furthermore, for face recognition  the ```Harcascade classifier``` was used. Harcascade is an open source Face recognition classifier which can be found on [Github](https://github.com/opencv/opencv/tree/master/data/haarcascades).


## Features
- Easy to set up: with just a few simple steps, you can get your PiCamera up and running and start tracking your face.

- Flexible: you can customize the code to suit your needs and add additional features. For example, you can adjust the sensitivity of the facial detection, or you can add support for multiple faces.

- Open-source: the code for PiCamera is available on GitHub, so you can download it, modify it, and share it with others. This allows the community to collaborate and improve the project, making it even more useful and powerful. 

- Compact design: the PiCamera is small and lightweight, making it easy to integrate into your projects. You can easily mount it on a tripod or attach it to your Raspberry Pi using a servo motor.



## Getting Started
To get started with PiCamera, you will need the following:

**Main Components**
- A Raspberry Pi with a camera module
- A servo motor
- A breadboard and jumper wires

For a detailed bill of material refer to the [Bill_Of_Materials.xlsx](https://github.com/moeb8001/facetrackingcamera/blob/main/Bill_Of_Materials.xlsx) in the Repository.

**Main Requirements**
You will also need to install the following software on your Raspberry Pi:

- The Python programming language
- The OpenCV library
- The Haarcascade
- You can find instructions for how to install these online


**Overview of steps taken**


First, you will need to connect the servo motor to your Raspberry Pi using the breadboard and jumper wires. You can find instructions for how to do this online, or you can refer to the instructions included with your servo motor.

Next, you will need to install the required software on your Raspberry Pi. This includes the Python programming language, the OpenCV library, and the Haarcascade. You can find instructions for how to install these online, or you can refer to the instructions included with your servo motor.

Once you have everything installed, you can download the PiCamera code from GitHub and run it on your Raspberry Pi. The code will automatically detect and track your face, moving the servo motor to keep the camera pointed at you.



## Conclusion
PiCamera is a fun and easy way to add facial tracking to your Raspberry Pi projects. Inspired by the Insta360 webcam, PiCamera allows you to quickly and easily add this advanced technology to your projects. With its simple setup and flexible code, you can start experimenting with facial tracking today and see what you can create!

(More clear explanations along with all the complete files will be added later when theyr are fuly done)
