import requests
#import json
#THIS WORKS FINE, you just gotta modify the environment to include This
# export DJANGO_SETTINGS_MODULE=RESTAPI.settings
#Found in: https://stackoverflow.com/questions/26082128/improperlyconfigured-you-must-either-define-the-environment-variable-django-set
#Api address
API_ADDRESS = 'http://192.168.1.29:8000/requests/'#default is supposed to be the PC's current ip address, should really abstract this out but whatever
IP_ADDRESS = '192.168.1.29'
PORT = '8000'
ADMIN = 'mec123'
PASS = 'mec123'


class API_CALL_HANDLER:

    def __init__(self, ip=IP_ADDRESS, port=PORT, api=API_ADDRESS, user=ADMIN, passw=PASS):
        self.ip_address = ip
        self.port = port
        self.api_address = api
        self.passw = passw
        self.user = user
        return

    def api_url(self):
        return 'http://'+self.ip_address+':'+str(self.port)+ '/' + self.api_address+'/'
    
    def post_api_url(self,uid=0):
        return self.api_url() +str(uid)+'/'

    def credentials(self):
        return (self.user,self.passw,)

    def send_response(self, uid=0, data={}):#will provide dummy data by default
        return requests.post( self.post_api_url(uid=uid), auth=self.credentials(), json=data)

    # may have over-engineered this
    def __enter__(self):
        self.__init__()
        return self

    def __exit__(self, exception_type, exception_value, traceback):

        return None
  
    def dummy_data(self):
        data = {'uid':10,
        'robot_to_send': 1,
        'executed':False,
        "joint_1": "0.62",
            "joint_2": "0.02",
            "joint_3": "0.10",
            "joint_4": "0.43",
            "joint_5": "0.23",
            "joint_6": "0.14"}
        return data

'''Returns a request response in text format'''
def receive_response():
    req = requests.get(API_ADDRESS)
    return req.text


def send_response(uid=0, data={}):
    req = requests.post(API_ADDRESS+str(uid)+'/' , auth=('mec123','mec123'), json=data)
    return req

# def main():
#     send_response(uid=10,data=dummy_data())
#     #print(receive_response())

# if __name__ == "__main__":
#     main()
