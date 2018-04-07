from rest_framework import serializers
from app.models import Student

class STSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__' #('post')
