from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import generics
from .models import Header, About, Education, Experience, Certification, Category, Blog, Video, Comment, Contact, Socials,Bookings
from .serializers import (HeaderSerializer, AboutSerializer, EducationSerializer, ExperienceSerializer,BookingSerializer, CertificationSerializer, CategorySerializer, BlogSerializer, VideoSerializer, CommentSerializer, ContactSerializer, SocialsSerializer)
import requests
from rest_framework import viewsets
from rest_framework import status
from django.utils import timezone
from PIL import Image, ImageDraw, ImageFont
from django.core.files.storage import FileSystemStorage
from config import settings
import os
from io import BytesIO
import pytz


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
          

from datetime import datetime, timedelta, time
class AvailableTimes(APIView):
    def get(self, request):
        # `date` parametrini olish
        date_param = request.GET.get('date')
        uzbekistan_tz = pytz.timezone('Asia/Tashkent')

# Hozirgi vaqtni O'zbekiston vaqti bilan olish
        booking_time = datetime.now(uzbekistan_tz).strftime('%d %B %Y, %H:%M')

        today = datetime.now(uzbekistan_tz).date()  # Lokal vaqtni olish
        now = datetime.now(uzbekistan_tz).time()    # Lokal vaqtni olish

        # Sanani o'qish yoki bugungi sanani olish
        if date_param:
            try:
                # Sanani `YYYY-MM-DD` formatida konvertatsiya qilish
                requested_date = datetime.strptime(date_param, "%Y-%m-%d").date()
            except ValueError:
                # Agar sanani to'g'ri formatda bermasa, bugungi sanani ishlatamiz
                requested_date = today
        else:
            requested_date = today

        all_possible_dates = self.get_all_possible_dates(requested_date)

        # Booked dates from database (only dates with times)
        booked_dates = Bookings.objects.values_list('date', flat=True)
        booked_dates = [datetime.combine(date.date(), date.time()).replace(tzinfo=None) for date in booked_dates]
        # print("Booked dates:", booked_dates)  # Debug print

        # Function to get available times for a given date
        def get_available_times(date):
            times = all_possible_dates.get(date, [])
            if date == today:
                # For today, filter out times before the current time
                times = [t for t in times if t >= now]
            # Exclude booked times
            available_times = []
            for t in times:
                combined_datetime = datetime.combine(date, t).replace(tzinfo=None)
                if combined_datetime not in booked_dates:
                    available_times.append(t.strftime("%H:%M"))
            return available_times

        # Function to check if a date is a Sunday
        def is_sunday(date):
            return date.weekday() == 6  # 6 - Sunday

        # Collect available times for the requested date
        available_times = get_available_times(requested_date)
        data = {
            "date": requested_date.strftime("%Y-%m-%d"),
            "times": available_times,
            "dates": [(
                (requested_date + timedelta(days=i)).strftime("%Y-%m-%d")
            ) for i in range(5)]
        }

        # Add message for Sunday
        if is_sunday(requested_date):
            data["message"] = "Dam olish kuni"

        # Add message if no times are available
        if not available_times:
            data["message"] = "Bu sana uchun mavjud vaqtlar mavjud emas"

        # Add success field
        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }

        return Response(response_data)

    def get_all_possible_dates(self, start_date):
        start_time = time(8, 0)  # 08:00
        end_time = time(14, 30)   # 15:00
        interval = timedelta(minutes=30)
        times = {}

        for i in range(5):  # Bugun va keyingi 4 kun
            current_date = start_date + timedelta(days=i)
            current_time = start_time
            if current_date not in times:
                times[current_date] = []
            while current_time <= end_time:
                times[current_date].append(current_time)
                current_time = (datetime.combine(current_date, current_time) + interval).time()

        return times
class CreateBooking(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            date_str = request.data.get('date')
            try:
                # Vaqt zonasini aniq belgilash
                date = timezone.make_aware(datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S'), timezone.get_current_timezone())
            except ValueError:
                return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)

            if Bookings.objects.filter(date=date).exists():
                return Response({'error': 'This time is already booked'}, status=status.HTTP_400_BAD_REQUEST)
            

            booking_instance = serializer.save()
            image_url = self.create_and_save_jpg({
                'name': request.data.get('name'),
                'phone': request.data.get('phone'),
                'date': date  # Formatted date object
            })

            return Response({
                            'success': True,
                            'message': 'Succes',
                            'data': {
                                'message': 'Tabriklaymiz! Siz roʻyxatga muvaffaqiyatli qabul qilindingiz. Marhamat, qabul ruxsatnomasini yuklab oling.',
                                'image_url': image_url
                            }
                        }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_and_save_jpg(self, data):
        # Define paths and filenames
        base_dir = settings.MEDIA_ROOT
        input_image_path = os.path.join(base_dir, 'book/1.jpg')
        file_name = f"booking_{timezone.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        output_image_path = os.path.join(base_dir, 'book', file_name)

        # Open and prepare the image
        image = Image.open(input_image_path)
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size

        # Load fonts
        try:
            title_font = ImageFont.truetype("arial.ttf", 80)
            body_font = ImageFont.truetype("arial.ttf", 50)
        except IOError:
            title_font = ImageFont.load_default()
            body_font = ImageFont.load_default()

        # Function to draw left-aligned text
        def draw_left_aligned_text(draw, text, y_position, font, max_width):
            lines = []
            words = text.split(' ')
            line = ""
            for word in words:
                test_line = f"{line} {word}".strip()
                text_bbox = draw.textbbox((0, 0), test_line, font=font)
                if text_bbox[2] > max_width - 100:  # Subtract margin from width
                    if line:
                        lines.append(line)
                    line = word
                else:
                    line = test_line
            if line:
                lines.append(line)
                
            x = 50  # Left margin
            for line in lines:
                text_bbox = draw.textbbox((0, 0), line, font=font)
                text_height = text_bbox[3] - text_bbox[1]
                draw.text((x, y_position), line, font=font, fill=(0, 0, 0))
                y_position += text_height  # Move to next line

        # Add title text
        title_text = "Qabul ruxsatnomasi"
        draw_left_aligned_text(draw, title_text, 500, title_font, image_width)

        # Format date and time
        formatted_date = format_date_uzbek(data['date'])
        formatted_time = data['date'].strftime('%H:%M')
        uzbekistan_tz = pytz.timezone('Asia/Tashkent')

# Hozirgi vaqtni O'zbekiston vaqti bilan olish
        booking_time = datetime.now(uzbekistan_tz).strftime('%d %B %Y, %H:%M')

        # Define text lines
        text_lines = [
            f"\t   Hurmatli {data['name']},\nSiz {formatted_date} kuni soat {formatted_time} ga",
            "qabulimga navbat band qildingiz. Fikringiz \noʻzgarsa, quyidagi raqamlarga boʻgʻlanib,",
            "ogohlantirib qoʻying. +998905142233",
            "Unutmang! Siz band qilgan vaqtda boshqa\nbemor qabulga yozilishi ham mumkin edi\n\n\n"

           
             f"Ro'yxatga olish vaqti:\n "
             f"\n\n{booking_time}"

            f"\n\nDoktor Azizjon Davlatovich\n\n\n\n"

           

        ]

        # Draw text lines
        current_y = 650
        for line in text_lines:
            draw_left_aligned_text(draw, line, current_y, body_font, image_width)
            current_y += 100

        # Save the updated image
        image.save(output_image_path)

        # Return the image URL
        image_url = os.path.join(settings.MEDIA_URL, 'book', file_name)
        
        # Schedule image deletion
        delete_after = timedelta(minutes=1)
        delete_time = timezone.now() + delete_after
        self.schedule_image_deletion(output_image_path, delete_time)

        return image_url

    def schedule_image_deletion(self, image_path, delete_time):
        # Schedule image deletion
        from threading import Timer

        def delete_image():
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Rasm o'chirildi: {image_path}")

        delay = (delete_time - timezone.now()).total_seconds()
        Timer(delay, delete_image).start()

def get_uzbek_month_name(month_number):
    months = {
        1: 'Yanvar',
        2: 'Fevral',
        3: 'Mart',
        4: 'Aprel',
        5: 'May',
        6: 'Iyun',
        7: 'Iyul',
        8: 'Avgust',
        9: 'Sentabr',
        10: 'Oktyabr',
        11: 'Noyabr',
        12: 'Dekabr'
    }
    return months.get(month_number, '')

def format_date_uzbek(date):
    day = date.day
    month = get_uzbek_month_name(date.month)
    year = date.year
    return f"{day} {month} {year}"