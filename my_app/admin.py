from django.contrib import admin
from .models import Header, About, Education, Experience, Certification, Category, Blog, Video, Comment, Contact, Socials

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'profession', 'name', 'experience', 'image')
    search_fields = ('title', 'profession', 'name')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')
    search_fields = ('title', 'number')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title', 'link')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    list_filter = ('status',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address', 'latitude', 'longitude')
    search_fields = ('phone', 'email', 'address')

@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'link')
    search_fields = ('name', 'link')
