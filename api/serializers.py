from rest_framework import serializers

from .models import Services, Testimonials, Team, Project, Blog


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class testimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
