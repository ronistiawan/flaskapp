import nexmo
from random import randint
from instance.config import NEXMO_KEY, NEXMO_SECRET, ENVIRONMENT

class SMS:
    client = nexmo.Client(key=NEXMO_KEY, secret=NEXMO_SECRET)        

    def send(phoneNumber, message):
        if ENVIRONMENT.__eq__('DEVELOPMENT'):
            print('TO: ',phoneNumber,'Message: ',message)
        else:
            SMS.client.send_message({'from': 'App','to': phoneNumber,'text': message,})

    def sendVerificationCode(phoneNumber):
        code = randint(100000,999999)
        if ENVIRONMENT.__eq__('DEVELOPMENT'):
            print('TO:',phoneNumber,'Message: Your verification code is', code)
        else:
            SMS.client.send_message({'from': 'App','to': phoneNumber,'text': 'Your verification code is '+code,})
        return code