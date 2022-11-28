from rest_framework import serializers
from taskapp.models import Cleint,Project,User

class CleintSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cleint
        fields=('Client_Id','Client_Name','Project_Name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('Id','Full_Name','Gmail','Phone','Password','Project_Name')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('Project_Id','Project_Name','Cleint_Name')