# USE Raspberry Pi to run Lane Detection
This project used Raspberry pi to run the Lane Detection with a USB camera.
## This is my first GitHub project
Two weeks ago I saw a blog on a Chinese knowledge share platform named 'ZhiHu', the title was 'Use raspberry pi to detect the road line on my car'

I thought that was pretty cool, so I decide to have some fun on that. so I followed the instruction to Github， create an account and forked the project.

The project I have cloned [click here](https://github.com/putcn/lane-detection-raspberry-pi). And I found he cloned and update from [here](https://github.com/uvbakutan/lane-detection-raspberry-pi)
, And uvbakutan have modificated/optimized version from the Udacity advanced-lane-detection project.

What I do in this project is both uvbakutan and putch
they all used picamera which is raspberryPi official on board camera, and this camera was suck, so I decide to try to Use USB camera to launch this program.


## Requirements
Firstly I bought a raspberryPi 3B+ and picamera 

![image](https://github.com/zhangcunxi/USE-Raspberry-Pi-run-Lane-Detection/blob/master/RaspberryPi.png)

And I found a USB camera at my home's storage room.

![image](https://github.com/zhangcunxi/USE-Raspberry-Pi-run-Lane-Detection/blob/master/USBCamera.png)

After that I have start to build my environments:

1. install newest raspbian on RP.
2. install OpenCV 3.4 this cost me about 8 hours for me and I followed [this link](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/) to make it successful. 

	>This instruction will use `virtualenv` a virtual environment  to install OpenCV,  **I highly recommend that.** About the reason [read this](https://realpython.com/python-virtual-environments-a-primer/)
3. install picamera
4. install imutils by this : ```pip install --upgrade imutils```

	>[imutils](https://github.com/jrosebr1/imutils) is developed by the blog writer who write 'how to install OpenCV on RP' , and I found this package has already integrate a class to use both picamera and USB camera. So, I will import this package to do my work.

## Software

1. The uvbakutan's project has create a class to detection the road lane, but when he use this class, he did not write `main()`function, so I update this module, this will ensure I can import this class in other place.
2. At the new python file I have import imutils and modify to use USB camera.
**So, please keep the 'lane_detection_with_USB_camera.py' in the same folder with 'lane_detect_pi.py'**

## Test
I have test this program by using video recorded from my safety recorder which setup on my car, and I have upload the test result video on this project.

The camera I've used was sensitive on light, so I have adjust my screen's light option make sure the video under my test was dark enough, like I said, just for fun~
