from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Header(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    image = models.ImageField(upload_to="header/image", verbose_name="Rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sarlavha"
        verbose_name_plural = "Sarlavhalar"

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    profession = models.CharField(max_length=200, verbose_name="Kasbi")
    name = models.CharField(max_length=200, verbose_name="Ism")
    experience = models.CharField(max_length=200, verbose_name="Tajriba")
    image = models.ImageField(upload_to="header/image", verbose_name="Rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Haqida"
        verbose_name_plural = "Haqida"

class Education(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ta'lim"
        verbose_name_plural = "Ta'lim"

class Experience(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tajriba"
        verbose_name_plural = "Tajriba"

class Certification(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    image = models.ImageField(upload_to="header/image", verbose_name="Rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = RichTextUploadingField(verbose_name="Tavsif")
    number = models.CharField(max_length=20, verbose_name="Raqam")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = RichTextUploadingField(verbose_name="Maqola matni")
    image = models.ImageField(upload_to="header/image", verbose_name="Rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"

class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    link = models.CharField(max_length=200, verbose_name="Havola")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"

class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    comment = RichTextUploadingField(verbose_name="Sharh matni")
    status = models.BooleanField(default=False, verbose_name="Holat")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Sharhlar"

class Contact(models.Model):
    phone = models.CharField(max_length=200, verbose_name="Telefon")
    email = models.CharField(max_length=200, verbose_name="Email")
    address = models.CharField(max_length=200, verbose_name="Manzil")
    latitude = models.CharField(max_length=200, verbose_name="Kenglik")
    longitude = models.CharField(max_length=200, verbose_name="Uzunlik")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Aloqa"
        verbose_name_plural = "Aloqalar"

class Socials(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    icon = models.ImageField(upload_to="icon/social", verbose_name="Ikona")
    link = models.CharField(max_length=200, verbose_name="Havola")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar"


class Bookings(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    phone = models.CharField(max_length=200, verbose_name="Telefon")
    date = models.DateTimeField(verbose_name="Sana")
    
    def __str__(self):
        return f"{self.name} - {self.date}"
    

    