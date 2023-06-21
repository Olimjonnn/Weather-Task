from rest_framework import serializers
from main.models import *


class InfoSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'