from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('urlApi/',views.CL_Url.as_view(),name='createurlapi'),
    path('urlApi/<str:url_id>',views.UDR_Url.as_view(),name='UDR'),
]