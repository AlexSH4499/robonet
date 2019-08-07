# Leap Motion Controller

---

## Classes
- RobotStructure
  > Class Methods
  - joints_default_position(self)
  - joints_limits(self)
  - joints(self)
  - joint_mins(self)
  - joint_maxs(self)
  - str_joints(self)
  - update_joint(self, updated_joint={})
  - max_of_joint(self, min_max_tuple=tuple())
  - min_of_joint(self, min_max_tuple=tuple())
  - assert_joint_limits(self, joint, value)
  - params(self)
  - __init__(self,uid=0, name="")
  - __len__(self)
  - __str__(self)
  
- CustomListener
  > Class Methods
  - on_init(self, controller)
  - on_disconnect(self, controller)
  - on_exit(self, controller)
  - __empty(self, li=[])
  - on_frame(self, controller)
  - state_string(self, state)
  - __init__(self, ip=IP_ADDRESS, port=PORT,api=API_ADDRESS,user=ADMIN,passw=PASS)

- Global Variables
    - IP_ADDRESS = '192.168.1.29'
    - PORT='8000'
    - API_ADDRESS='requests'
    - ADMIN='mec123'
    - PASS='mec123'
    - FRAME_BUFFER_LIM = 14
    - fingers = [ ]
---

## RobotStructure
> Class Method Descriptions
  - joints_default_position(self)
  >> Returns a list of tuples containing each joint and a coordinate for the joint in radians (defaults to 0.0)

  - joints_limits(self)
  >> Returns a generator that yields limits(defined in joint_mins/maxs) from a dictionary (key is the name as a string, value is the tuple pair(min,max) of floating point numbers)
  
  - joints(self)
  >> Returns the internal list(length is 6) of joints (floating point numbers)
  
  - joint_mins(self)
  >> Returns a generator that yields hardcoded minimum limits from a list (floating point numbers)
  
  - joint_maxs(self)
  >> Returns a generator that yields hardcoded maximum limits from a list (floating point numbers)
  
  - str_joints(self)
  >> Returns a generator that yields hardcoded names of joints from a list (strings)
  
  - update_joint(self, updated_joint={})
  >> Receives a dictionary representing a joint(key is the name as a string, value is the floating point number) and its new value to update the internal dictionary.
  
  - max_of_joint(self, min_max_tuple=tuple())
  >> Receives a tuple with both min and max of a joint and returns the maximum (floating point number)
  
  - min_of_joint(self, min_max_tuple=tuple())
  >> Receives a tuple with both min and max of a joint and returns the minimum (floating point number)
  
  - assert_joint_limits(self, joint, value)
  >> Receives a joint name(string) and a value (floating point number) and verifies that the value does not surpass the limits from joint_limits
  >> If the limits are passed, it defaults the value to whichever is closer to the value provided
  
  - params(self)
  >> Returns a list (strings) representing the internal data of the class
  >> This is used to create the JSON that is sent to the REST API
  
  - __init__(self,uid=0, name="")
  >> Called when creating a new Object and initializes the instance variables:
  >>  - uid - signed integer to identify the robot, defaults to 0 when not provided
  >>  - name - string representation for name  of the robot, defaults to an empty string when not provided
  >> - _ joints - Ordered dictionary initialized to defaults of _**joints_default_position**_ method
  
  - __ len __ (self)
  >> Returns a length of '1' to let us iterate through lists of this object if needed
  
  - __ str __ (self)
  >> Returns a string representation of the instance of _RobotStructure_ when using _**str**_ or _**print**_ standard library methods

---

---

## CustomListener
> Class Method Descriptions

  - on_init(self, controller)
  >> Runs automatically when the script is executed and begins doing calls to Leap SDK
  
  - on_connect(self, controller)
  >> Runs automatically when the Leap Motion sensor is connected and awaits _on_frame_ method
  
  - on_disconnect(self, controller)
  >> Runs automatically when the Leap Motion sensor is disconnected and ends any calls to Leap SDK
  
  - on_exit(self, controller)
  >> Runs when the program is exited after pressing 'Enter' key
  
  - __ empty(self, li=[])
  >> Empties out the _li_ provided, but it's only used to empty our internal buffer from __ init __ method. Could be repurposed to use any mutable iterable realistically
  
  - on_frame(self, controller)
  >> Executed automatically everytime a movement is registered from LeapMotion sensor
  >> This is where all the processing of the Hand objects occurs and calls to RobotStructure are handled.
  
  - __ init __ (self, ip=IP_ADDRESS, port=PORT,api=API_ADDRESS,user=ADMIN,passw=PASS)
  >> Called when creating a new Object and initializes the instance variables:
  >>  - port - signed integer to identify the robot, defaults to PORT when not provided
  >>  - ip - string representation for IP address  of the REST API, defaults to an IP_ADDRESS when not provided
  >>  - user - string representation for user of the REST API, defaults to an ADMIN when not provided
  >>  - passw - string representation for passw of the REST API, defaults to an PASS when not provided
  >>  - api - string representation for API url  of the REST API, defaults to an API_ADDRESS when not provided


---

## Functions
- convert_to_joints(properties)
>> Receives the properties from Hand object given by Leap Motion sensor and returns a tuple of 6  joint values (floating point numbers)

- hand_properties(frame)
>> Extracts the Hand object's properties from a Frame of the Leap Motion sensor
>> Returns a  tuple of seven properties: x,y,z, pitch, yaw, roll, finger_yaw

- main(ip='192.168.1.29', port=8000, api='requests', user='mec123',passw='mec123')
>> Handles the logic of the sensor when the script gets executed, receives IP,port and route of API along with authentication. 

