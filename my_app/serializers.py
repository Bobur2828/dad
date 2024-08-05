from rest_framework import serializers
from .models import (Header, About, Education, Experience, Certification, Category, Blog, Video, Comment, Contact, Socials,Bookings)

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['id', 'title', 'image']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'profession', 'name', 'experience', 'image']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'title']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'title']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'title', 'image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'number']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'image']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'link']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'comment', 'status']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'phone', 'email', 'address', 'latitude', 'longitude']

class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = ['id', 'name', 'icon', 'link']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'
