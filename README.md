# Robonet
<p>This is a small project for the 2019 Summer Internship at V-Team.
  The aim of this project is to provide a use case for future telecommunications technologies and their impact on unmmanned or remotely manned systems.
</p>
<p>Important:
  This project runs on two versions of Python due to incompatibility with Leap Motion SDK and Python 3.0.
  I tried to compile the SDK from source with no fruits on Windows and ran into problems when trying on Ubuntu Linux Subsystem thanks to to lack of daemon functionality. My apologies for the shortcomings on this part of the project but I really tried my best given my time constraints.</p>
  
## Libraries(or dependencies)
- Django
- Django Rest Framework
- requests (Python 3 and 3.7)
- coreapi
- Leap Motion SDK
- Niryo One Python API(python 2.7)

# How to run
<div>
<p style="text:bold">
  Requirements
  </p>
  <li>
    <ul>Python 2.7.x & Python 3.7.x
    </ul>
    <ul>SSH</ul>
    <ul>
      requests
    </ul>
    <ul>
      django & django-restframework
    </ul>
    <ul>router or LAN available</ul>
    <ul> virtualenv (comes with Python 3 already)</ul>
  </li>
  </div>
  
<p>
  Open a terminal and change into the directory for this project.
  Activate virtualenv for Python  2.7 and proceed to change directory into RESTAPI folder.
  Once inside the folder, execute the command "python manage.py runserver 192.168.1.21:8000".
  This command will make the HTTP server run on port 8000 such that we can communicate with it using our robot.
  Now that it's running we can open up another terminal, change again into the projects main folder and when inside activate a Python 3.7.x+ environment. Once this step is finished, execute the following command "python leap_motion_controller.py" and this will cause the terminal to seek the Leap Motion USB device. Wait until the terminal says "Connected" to confirm that we are properly communicating with it.(Sometimes the Leap SDK ignores the USB device and requires a fresh install.) After establishing the connection, open yet another terminal and SSH
  into the Niryo robot using the command "ssh niryo@ip_address" in my case I setup the IP Address to be 192.168.1.53 in order to ensure that both, computer and robot, were on the same network as per IPv4 protocol.(Assume the Subnet-Mask to be 24-bits)
  </p>
