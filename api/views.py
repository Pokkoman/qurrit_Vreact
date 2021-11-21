from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Program
from .serializers import ProgramSerializer
# Create your views here.

def index(request):
    return HttpResponse("hello ")

@api_view(['GET'])
def getProgram_list(request):
    
    program_list= Program.objects.all()
    program_list_serializer = ProgramSerializer(program_list,many = True)

    return Response(program_list_serializer.data)
