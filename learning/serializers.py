from rest_framework import serializers
from .models import  HomeNav,Schools

class NavSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeNav
        fields = '__all__'



from rest_framework import serializers
from .models import Schools

class StudentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'
        
from rest_framework import serializers
from .models import  HomeNav

class NavSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeNav
        fields = '__all__'


