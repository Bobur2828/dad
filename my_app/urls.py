from django.urls import path
from .views import HeaderView,Service,BlogView,AvailableTimes, CreateBooking, CommentCreate, CommentList

urlpatterns = [
    path('view_header/', HeaderView.as_view(),name="Contact Malumotlari"),
    path('view_service/', Service.as_view(),name="Contact Malumotlari"),
    path('view_blog/', BlogView.as_view(),name="Contact Malumotlari"),
    path('available_times/', AvailableTimes.as_view(), name='available_times'),
    path('create_booking/', CreateBooking.as_view(), name='create_booking'),
    path('comment_create/', CommentCreate.as_view(), name='create_comment'),
    path('comment_list/', CommentList.as_view(), name='comment_list'),


]
