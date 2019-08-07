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
  - __len__(self)
  - __str__(self)

---
## Functions
- convert_to_joints(properties)
- hand_properties(frame)
- main(ip='192.168.1.29', port=8000, api='requests', user='mec123',passw='mec123')

