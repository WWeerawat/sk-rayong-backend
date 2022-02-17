from rest_framework import serializers
from .models import Lock, LockImage, Nearyby, Phase, PhaseImage


class LockImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LockImage
        fields = ["id", "image"]


class NearybySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nearyby
        fields = "__all__"


class LockSerializer(serializers.ModelSerializer):
    images = LockImageSerializer(many=True, read_only=True)
    nearbies = NearybySerializer(many=True, read_only=True)

    class Meta:
        model = Lock
        fields = "__all__"


class PhaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhaseImage
        fields = ["id", "image"]


class PhaseSerializer(serializers.ModelSerializer):
    images = PhaseImageSerializer(many=True, read_only=True)
    phase_lock = LockSerializer(many=True, read_only=True)

    class Meta:
        model = Phase
        fields = "__all__"
