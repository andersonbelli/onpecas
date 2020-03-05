from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (req):
  return render(req,'index.html')

def details (req):
  return render(req,'single-product-details.html')

def aboutus (req):
  return render(req, 'blog.html')

def contact (req):
  return render(req, 'contact.html')