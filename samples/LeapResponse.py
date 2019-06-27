import requests
#import json
#THIS WORKS FINE, you just gotta modify the environment to include This
# export DJANGO_SETTINGS_MODULE=RESTAPI.settings
#Found in: https://stackoverflow.com/questions/26082128/improperlyconfigured-you-must-either-define-the-environment-variable-django-set
#Api address
API_ADDRESS = 'http://127.0.0.1:8000/requests/'

def dummy_data():
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
    #req = requests.post(API_ADDRESS+f'/{uid}'+'/post/' , auth=('mec123','mec123'), json=data)
    print(data)
    req = requests.post(API_ADDRESS+str(uid)+'/' , auth=('mec123','mec123'), json=data)
    # print(req.url)
    # print(req.data)
    # print(req.json  )
    return req

def main():
    send_response(uid=10,data=dummy_data())
    #print(receive_response())

if __name__ == "__main__":
    main()
