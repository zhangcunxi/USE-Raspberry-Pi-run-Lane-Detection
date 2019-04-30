# USE Raspberry Pi run Lane Detection

This project used Raspberry pi to run the Lane Detection with USB camera.

## This is my first GitHub project

Two weeks ago I have see a blog on Chinese knowlage share platform named 'ZhiHu',title is 'Use raspberry pi to detect the road line on my car'

I thought that preety cool, so I decide to have some fun on that. so I followed the instruction to Github regist account and fork the project.

The project I have cloned [click here](https://github.com/putcn/lane-detection-raspberry-pi). And I found he cloned and update from [here](https://github.com/uvbakutan/lane-detection-raspberry-pi)
, And uvbakutan have modificated/optimized version from the Udacity advanced-lane-detection project.

What I do in this project is both uvbakutan and putch
they all used picamera which is raspberryPi officiall on board camera, and this camera was suck, so I decide to try to Use USB camera to launch this programe.


## requirements
Firstly I bought a raspberryPi 3B+ and picamera 

![image](http://github.com/itmyhome2013/readme_add_pic/raw/master/images/nongshalie.jpg)

And I found a USB camera at my home storage room.

![image](http://github.com/itmyhome2013/readme_add_pic/raw/master/images/nongshalie.jpg)

After that I have start to build my enviroments:

1. install newest raspbian on RP.
2. install picamera
3. install OpenCV 3.4 this cost me about 8 hours for me and I followed [this link](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/) to make it successfull. 

	>This instruction will use `virtualenv` a virtual environment  to install OpenCV,  **I highly recommend that.** About the reason [read this](https://realpython.com/python-virtual-environments-a-primer/)

4. install imutils by this : ```pip install --upgrade imutils```

	>[imutils](https://github.com/jrosebr1/imutils) is developed by the blog writer who write 'how to install OpenCV on RP' , and I found this pakage has already integrate a class to use both picamera and USB camera. So, I will use this pakage to do my work.

##Software

1. The uvbakutan's project has create a class to detection the road lane, but when he use this class, he did not write `main()`function, so I update this module, this will ensure I can import this class in other place.
2. At the new python file I have import imutils and modify to use USB camera.
