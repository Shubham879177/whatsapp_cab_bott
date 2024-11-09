from .whatsappBott import WhatsappBott,User
# from twilio.rest import Client

class Templates:
    templates_data = {
    "greetmessage":"HXf302dc475c37eb666454b55a82f9beda"
    }
    @staticmethod
    def greetMessage(name):
        print("ok")
        content_variables = {"1":str(name)}
        
        return (Templates.templates_data.get("greetmessage"),content_variables)
        


def respondToMessage(messagedata):
    message:str = messagedata.get('Body')
    print(message)
    whatsapp_bott = WhatsappBott()
    if message.casefold() == "Hii".casefold():
        profilename = messagedata.get('ProfileName')
        waId  = messagedata.get('WaId')
        print(profilename,waId)
        template_data = Templates.greetMessage(profilename)
        print(template_data)
        user = User()
        user.setName(profilename)
        user.setPhoneNumber(waId)
        print(user)
        whatsapp_bott.setUser(user)
        whatsapp_bott.sendMessages(template_data[0], profilename)


