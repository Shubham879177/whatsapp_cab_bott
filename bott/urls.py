from django.urls import path

from whatsapp_bott.bott import views

path('',views.index, name="index")