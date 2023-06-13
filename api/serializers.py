from rest_framework import serializers

from .models import Services,Testimonials


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class testimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'
