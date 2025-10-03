from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
  """
  A simple view that returns "Hello World" for testing purposes.
  """
  return HttpResponse("Hello, world!")
