#!/bin/bash
ssh niryo@192.168.1.42 'source ~/catkin_ws/devel/setup.bash && export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api && python niryo_one_example_python_api.py'
