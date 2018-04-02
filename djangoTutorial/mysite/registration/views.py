from django.shortcuts import render
from django.http import HttpResponse
from .models import Voter
from django.core.exceptions import *

def index(request):
    return render(request, 'registration/check.html')

def allow(request):
    if request.method == 'POST':
        num = int(request.POST.get('textfield', None))
        try:
            user = Voter.objects.get(voter_number = num)
            html = (user)
            return HttpResponse(html)
        except Voter.DoesNotExist:
            return HttpResponse("Voter not registered in system.")
    else:
        return render(request, 'registration/check.html')
