from django.db import models
from django.db.models import fields
from rest_framework import serializers, validators
from .models import Logs


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields='__all__'
# class LogSerializer(serializers.Serializer):
#     local_id=serializers.BigIntegerField()
#     device_address=serializers.CharField(max_length=50)
#     c02=serializers.FloatField()
#     tv02=serializers.FloatField()
#     pm25=serializers.FloatField()
#     pm10=serializers.FloatField()
#     read_at=serializers.DateTimeField()
#     created_at=serializers.DateTimeField(auto_now_add=True)


# def create(self,validated_data):
#     return Logs.objects.create(validated_data)

# def update(self,instance,validated_data):
#     instance.local_id=validated_data.get('local_id',instance.local_id)
#     instance.device_address=validated_data.get('device_address',instance.device_address)
#     instance.c02=validated_data.get('c02',instance.c02)
#     instance.tv02=validated_data.get('tv02',instance.tv02)
#     instance.pm25=validated_data.get('pm25',instance.pm25)
#     instance.pm10=validated_data.get('pm10',instance.pm10)
#     instance.read_at=validated_data.get('read_at',instance.read_at)
#     instance.created_at=validated_data.get('created_at',instance.created_at)
#     instance.save()
#     return instance