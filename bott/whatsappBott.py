from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

class User:
    def __init__(self,):
        self.name = None
        self.phone_number = None

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number
    
    def setName(self, name):
        self.name = name

    def getPhoneNumber(self):
        return self.phone_number
    
    def getName(self):
        return self.name
    

    
    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}"
    

class WhatsappBott:
    def __init__(self):
        self.user = None

    def setUser(self, user):
        self.user = user
    
    def sendMessages(self, content_sid,content_variables):
        self.__sendMessage__(content_sid, content_variables)
        print(f"Sending message to {self.user.getName()}: {content_sid}")
    
    def __sendMessage__(self,content_sid,content_variables):
        print(content_sid,self.user.getPhoneNumber())
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid=f'{content_sid}',
        content_variables=content_variables,
        to=f'whatsapp:+{self.user.getPhoneNumber()}'
        )
        print(message.sid)


