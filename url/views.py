from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .serializer import *
from .models import *
# Create your views here.
class CL_Url(GenericAPIView,CreateModelMixin,ListModelMixin):

	queryset=Url.objects.all()
	serializer_class=UrlSerializer

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

class UDR_Url(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Url.objects.all()
    serializer_class=UrlSerializer
    lookup_field = 'url_id'

    # authentication_classes=[SessionAuthentication]


    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
    	return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
    	return self.destroy(request,*args,**kwargs)


