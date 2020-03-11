from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (req):
  return render(req,'index.html')

def details (req):
  return render(req,'single-product-details.html')