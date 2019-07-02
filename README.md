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
- Django
- Django Rest Framework
- requests (Python 3 and 2.7)
- coreapi
- Leap Motion SDK
- Niryo One Python API (Python 2.7)

---

# How to run

**Requirements**
  
- SSH
- Router or LAN available
- Python 2.7.x & Python 3.7.x
- virtualenv (comes with Python 3 already)
- requests
- django
- django-restframework

  
---
  
**NOTE**
_This portion makes the assumption that all necessary packages have been previously installed with pip._


>Open a terminal and change into the directory for this project.

>Activate virtualenv for Python  2.7 and proceed to change directory into RESTAPI folder.

>Once inside the folder, execute the command "python manage.py runserver 192.168.1.21:8000".

>This command will make the HTTP server run on port 8000 such that we can communicate with it using our robot.

>Now that it's running we can open up another terminal, change again into the project's main folder and when inside activate a Python 3.7.x+ environment.

>Once this step is finished, execute the following command "python leap_motion_controller.py" and this will cause the terminal to seek the Leap Motion USB device.

_If you're encountering problems, **verify** that your **environment variable (or PATH)** has the proper **Python & Python version active**._

>Wait until the terminal says "Connected" to confirm that we are properly communicating with the Leap Motion sensor.

_Sometimes the **Leap SDK ignores** the USB device and requires a **fresh install**._

>After establishing the connection, open yet another terminal and open an SSH connection
  to the Niryo robot using the command "ssh niryo@{ip_address_here}".
  
_Replace **{ip_address_here}** with the IP Address of your choice but be mindful that both must be kept within the same LAN or ensure a properly established connection between Computer & Robot._
  
 _In my case, I setup the **IP Address** to be **192.168.1.53** in order to ensure that both, computer and robot, were on the same network as per IPv4 protocol.(Assume the Subnet-Mask to be 24-bits)_

# Known Problems

- Leap Motion Python API has a **memory leak** problem where iterating through **Hand parameters** causes **infinite looping**.

> Possible fix: Implement a **double-underscore-len method** (deunder or magic method as known in Python community) since it seems that LeapPython.cpp does not properly generate with the one provided the in download from official site.

- Leap Motion SDK randomly decides to stop working and won't detect the Leap Motion Sensor.

> Possible fix: Reinstallation of Official SDK seems to fix this issue on Windows OS'.
