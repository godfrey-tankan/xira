from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home_view(request):
    return JsonResponse({'message': 'Home!'})