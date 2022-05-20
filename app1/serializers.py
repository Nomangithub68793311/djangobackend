from rest_framework import serializers
from app1.models import team
class Adddataserializer(serializers.ModelSerializer):
       class Meta:
        model = team
        fields = ['id', 'fullname', 'agelimit', 'sons','emailadd', 'password', 'occupation']