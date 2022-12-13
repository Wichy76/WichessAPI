from rest_framework import serializers

from .models import *


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardModel
        fields = ('id', 'FEN', 'theme', 'created_at')
        read_only_fields = ('created_at',)


class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningModel
        fields = ('id', 'name')


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerModel
        fields = ('id', 'difficulty', 'stereotype')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = ('id', 'opening', 'trainingMode', 'score', 'PGN', 'created_at')
        read_only_fields = ('created_at',)
