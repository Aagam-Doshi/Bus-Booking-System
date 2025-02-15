from django.urls import path    
from . import views

urlpatterns = [
    path('browsedetail/booking/<int:id>/',views.booking,name='booking'),
    path('', views.home, name ='blog-home'),
    path('about/', views.about, name ='blog-about'),
    # path('new-booking/',,name='user')
    # path('view-bookings/',,name='view-booking')
    path('browse/',views.browse),
    path('browsedetail/',views.browse_with_details),
    
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    # path('register/', views.register, name='register'),
    # path('verify_otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
    
]