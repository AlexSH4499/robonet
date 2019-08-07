# Leap Response

## Classes

  - API_CALL_HANDLER
  - Global Variables
    - API_ADDRESS = 'http://192.168.1.29:8000/requests/'
    - IP_ADDRESS = '192.168.1.29'
    - PORT = '8000'
    - ADMIN = 'mec123'
    - PASS = 'mec123'
    
##Class Methods
 - send_response(self, uid=0, data={})
 >> Receives data from and OrderedDictionary and a uid and sends a POST request to API with credentials as a JSON 
 
 - credentials(self)
 >> Returns the instantiated user and passw values
 
 - post_api_url(self,uid=0)
 >> Returns a string representing the API to which we POST based on received uid
 
 - api_url(self)
 >> Returns a string representing the API address provided in __ init __
 
 - __init__(self, ip=IP_ADDRESS, port=PORT, api=API_ADDRESS, user=ADMIN, passw=PASS)

  >> Called when creating a new Object and initializes the instance variables:
  >>  - ip - string representation of the REST API ip address on the network, defaults to IP_ADDRESS when not provided
  >> port - unsigned integer representing the port of the REST API on the network, defaults to PORT when not provided
  >>  - api - string representation for REST API entry point, defaults to an empty string when not provided
  >> - user - string representation for user  of the REST API, defaults to ADMIN when not provided
  >>  - pasw - string representation for password of  REST API entry point, defaults to PASS when not provided
