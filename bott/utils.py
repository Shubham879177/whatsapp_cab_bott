import json
from .whatsappBott import WhatsappBott,User
from .constants import greetmessages
# from twilio.rest import Client

class Templates:
    templates_sid = {
    "greetmessage":"HXf302dc475c37eb666454b55a82f9beda"
    }
    @staticmethod
    def greetUser(name):
       
        content_variables = {"1":str(name)}
        
        return (Templates.templates_sid.get("greetmessage"),content_variables)
        


def respondToMessage(messagedata):
    message:str = messagedata.get('Body')
    
    whatsapp_bott = WhatsappBott()
    if message.casefold() in greetmessages:
        profilename = messagedata.get('ProfileName')
        waId  = messagedata.get('WaId')
        template_data = Templates.greetUser(profilename)
        user = User()
        user.setName(profilename)
        user.setPhoneNumber(waId)
        whatsapp_bott.setUser(user)
        whatsapp_bott.sendMessages(template_data[0], json.dumps(template_data[1]))
    