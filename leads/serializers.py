from rest_framework import serializers
from .models import Contact_lead



class Contact_leadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_lead
        fields = '__all__'
        
        