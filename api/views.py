from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class BoardViewSet(viewsets.ModelViewSet):
    queryset = BoardModel.objects.all()

    serializer_class = BoardSerializer


class OpeningViewSet(viewsets.ModelViewSet):
    queryset = OpeningModel.objects.all()

    serializer_class = OpeningSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = ComputerModel.objects.all()

    serializer_class = ComputerSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all()

    serializer_class = GameSerializer
