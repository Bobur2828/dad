from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import generics
from .models import Header, About, Education, Experience, Certification, Category, Blog, Video, Comment, Contact, Socials
from .serializers import (HeaderSerializer, AboutSerializer, EducationSerializer, ExperienceSerializer, CertificationSerializer, CategorySerializer, BlogSerializer, VideoSerializer, CommentSerializer, ContactSerializer, SocialsSerializer)
import requests
from rest_framework import viewsets
from rest_framework import status



class HeaderView(APIView):
    def get(self,request):
        header = Header.objects.all()
        about = About.objects.all()
        education = Education.objects.all()
        experience = Experience.objects.all()
        certification = Certification.objects.all()
        headerSR=HeaderSerializer(header,many=True,context={'request': request})
        aboutSR=AboutSerializer(about,many=True,context={'request': request})
        experienceSR=ExperienceSerializer(experience,many=True,context={'request':request})
        educationSR=EducationSerializer(education,many=True,context={"request":request})
        certificationSR=CertificationSerializer(certification,many=True,context={'request': request})


        data={
            'header': headerSR.data,
            'about': aboutSR.data,
            'education': educationSR.data,
            'experience': experienceSR.data,
            'certification': CertificationSerializer(certification,many=True,context={'request': request}).data
        }

        response_data = {  # Response obyekti orqali JSON javob qaytarish
            'success': True,  # Operatsiyaning muvaffaqiyatli ekanligini bildiradi
            'message': "Success",  # Muvaffaqiyatli xabar
            'data':data
        }
        return Response(response_data)  # JSON javob qaytarish

class Service(APIView):
    def get(self, request):
        category_id = request.query_params.get('id', None)
        
        if category_id:
                category = Category.objects.get(id=category_id)
                serializer = CategorySerializer(category, context={'request': request})

                data = {
                     'service': serializer.data
                }
                response_data = {  # Response obyekti orqali JSON javob qaytarish
                            'success': True,  # Operatsiyaning muvaffaqiyatli ekanligini bildiradi
                            'message': "Success",  # Muvaffaqiyatli xabar
                            'data':data
                        }
                return Response(response_data)  # JSON javob qaytarish

        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True, context={'request': request})
        
            data = {
                     'service': serializer.data
                }
            response_data = {  # Response obyekti orqali JSON javob qaytarish
                            'success': True,  # Operatsiyaning muvaffaqiyatli ekanligini bildiradi
                            'message': "Success",  # Muvaffaqiyatli xabar
                            'data':data
                        }
            return Response(response_data)  # JSON javob qaytarish
        
class BlogView(APIView):
    def get(self, request):
        blog_id = request.query_params.get('id', None)
        
        if blog_id:
            try:
                blog = Blog.objects.get(id=blog_id)
                serializer = BlogSerializer(blog, context={'request': request})
                data = {'blog': serializer.data}
                response_data = {
                    'success': True,
                    'message': "Success",
                    'data': data
                }
                return Response(response_data)
            except Blog.DoesNotExist:
                response_data = {
                    'success': False,
                    'message': "Blog not found",
                    'data': {}
                }
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        else:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True, context={'request': request})
            data = {'blog': serializer.data}
            response_data = {
                'success': True,
                'message': "Success",
                'data': data
            }
            return Response(response_data)
          