from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .parts_serializers import PartsSerializer
from .models import Parts

#########################
#from django.shortcuts import render

#from rest_framework import viewsets

#from .serializers import PartsSerializer
#from .models import Parts
#########################

# Create your views here.
class PartsViewSet(viewsets.ModelViewSet):
	queryset = Parts.objects.all().order_by('name')
	serializer_class = PartsSerializer
