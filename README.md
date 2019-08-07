# Robonet
<p>This is a small project for the 2019 Summer Internship at V-Team.
  The aim of this project is to provide a use case for future telecommunications technologies and their impact on unmmanned or remotely manned systems.
</p>

---

**Important**
  
  This project runs on **two** versions of **Python** due to incompatibility with Leap Motion SDK and Python 3.X.X .
  I tried to compile the SDK from source with no fruits on Windows and ran into problems when trying on Ubuntu Linux Subsystem thanks to  lack of daemon functionality. My apologies for the shortcomings on this part of the project but I really tried my best given my time constraints.
  
---

### Scope & Areas of Interest

> This project covers server backend, networking and high level application development (Layers 4-7 on OSI Model).

---

## Libraries(or dependencies)
---
- requests (Python 3 and 2.7)
- coreapi
- Leap Motion SDK
- Niryo One Python API (Python 2.7)
- virtualenv (comes with Python 3 already)
- requests
- django
- django-restframework
- paramiko (Python 2.7)[This is a commodity and not a necessity for transferring the scripts onto the robot]

---

# How to run

**Requirements**

---

- SSH or equivalent on Windows
- Router or LAN available (Any OSI Layer 3 device should suffice)
- Python 2.7.x & Python 3.7.x

---
  
**NOTE**
_This portion makes the assumption that all necessary packages have been previously installed with pip._

## Setting up HTTP Server

>Open a terminal and change into the directory for this project.

>Activate virtualenv for Python  2.7 and proceed to change directory into RESTAPI folder.

>Once inside the folder, execute the command "python manage.py runserver {your_computers_ip}:8000".

>This command will make the HTTP server run on port 8000 such that we can communicate with it using our robot.

**IMPORTANT** 

_The IP Address {your_computers_ip} affects how the scripts behave so make sure to change the variables:_
- ip, port in leap_motion_controller.py
- server_ip from  **if __name__ == "__main__"** in niryo_one_python_example.py
## Connecting to Leap Motion Controller 

---

>To Run leap_motion_controller.py make sure to be using Python 2.7 virtualenv

_Ensure the script is in same directory as Leap Motion Developer Kit. Note, this script is designed to run on Windows OS due to src_dir(assumes  SDK is installed directly on C drive) variable and path insertion of SDK using Windows style directories(at the top of file). If you wish to run this in Linux, make the appropriate changes to src_dir and the path insertion at the top of the python script file._

---
** NOTE** 
> This file is under the assumption that the LeapSDK used is installed in the path for windows as:

>> _C:\\LeapDeveloperKit_2.3.1+31549_win\\LeapSDK\\lib\\x64_ (this assumes the system being utilized is x64, make changes accordingly)
---

> Run the command _python leap_motion_controller.py_ in the commandline.

_If you're encountering problems, **verify** that your **environment variable (or PATH)** has the proper **Python & Python version active**._

> Wait until the terminal says "Connected" to confirm that we are properly communicating with the Leap Motion sensor.

- _Sometimes the **Leap SDK ignores** the USB device and requires a **fresh install**._
---



## Connecting to the Niryo Robot
---
> After establishing the connection with LeapMotion controller, open yet another terminal and establish an SSH connection
  to the Niryo robot using the command "ssh niryo@{ip_address_here}".
  
_Replace **{ip_address_here}** with the IP Address of the robot on the network but be mindful that both must be kept within the same LAN or ensure a properly established connection between Computer & Robot._
  
 _In my case, I setup the **IP Address** to be **192.168.1.x** in order to ensure that both, computer and robot, were on the same network as per IPv4 protocol.(Assume the Subnet-Mask to be 24-bits)_
 
 **IMPORTANT**
 _The IP Address {ip_address_here} affects how the scripts behave so make sure to change the variables:_
 - ROBOT_IP_ADDRESS in _ssh_file_transfer.py_

---

# Known Problems

- Leap Motion Python API has a **memory leak** problem where iterating through **Hand parameters** causes **infinite looping**.

> Possible fix: Implement a **double-underscore-len method** (deunder or magic method as known in Python community) since it seems that LeapPython.cpp does not properly generate with the one provided the in download from official site.

- Leap Motion SDK randomly decides to stop working and won't detect the Leap Motion Sensor.

> Possible fix: Reinstallation of Official SDK seems to fix this issue on Windows OS'.

- __launch.sh__ won't run in Linux environment due to being created originally on Windows (saved as a DOS format)
> Fix: Copy paste the contained info into a new file then, run the command __chmod +x "filename"__ to make it executable
