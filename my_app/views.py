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

