from django.urls import path
from .views import HeaderView,Service,BlogView

urlpatterns = [
    path('view_header/', HeaderView.as_view(),name="Contact Malumotlari"),
    path('view_service/', Service.as_view(),name="Contact Malumotlari"),
    path('view_blog/', BlogView.as_view(),name="Contact Malumotlari"),



]
