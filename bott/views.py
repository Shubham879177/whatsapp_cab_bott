from django.http import HttpResponse,JsonResponse,HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import respondToMessage



def home(request):
    return HttpResponse("Welcome to the homepage!")


@csrf_exempt
def webhook_get(request):
    query = request.GET.get('hub.challange')
    print("test click")
    return HttpResponse(query)


@csrf_exempt
def webhook_post(request):

   respondToMessage(request.POST)
   print("click")
   
   return HttpResponse("Webhook post request received successfully!")
   