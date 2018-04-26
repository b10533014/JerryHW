from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Introduction

# Create your views here.
def index(request):
    introduction111 = Introduction.objects.all()
    return render_to_response('annie/menu.html',locals())
	