# Niryo One Example Python API
- Global Variables
  - API_ROOT = 'http://192.168.1.29:8000/requests/
  
## Functions

- debugging(server_ip, server_port, api_point, username,passw)
>> Runs an infinite loop while constantly requesting data from REST API


- movements(json_data=[])
>>  Returns a list of extracted movement data

- extract_movement(data={})
>> Extracts the robot movement data from the JSON of REST API GET request

- cleanse_data(req)
>> Eliminates unnecessary data from JSON of req

- open_connection_to_API(api=API_ROOT)
>> Instantiates an HTTP GET Request to the  api provided or defaults to API_ROOT
