from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Nearyby, Phase, Lock
from .serializers import NearybySerializer, PhaseSerializer, LockSerializer

# Create your views here.
@api_view(["GET"])
def getAllPhase(req):
    phases = Phase.objects.all()
    serializer = PhaseSerializer(phases, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getPhase(req, pk):
    phases = Phase.objects.get(id=pk)
    serializer = PhaseSerializer(phases, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getAllLock(req):
    locks = Lock.objects.all()
    serializer = LockSerializer(locks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getLock(req, pk):
    lock = Lock.objects.get(id=pk)
    serializer = LockSerializer(lock, many=False)
    return Response(serializer.data)
