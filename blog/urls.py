from django.urls import path    
from . import views

urlpatterns = [
    path('', views.home, name ='blog-home'),
    path('about/', views.about, name ='blog-about'),
    # path('new-booking/',,name='user')
    # path('view-bookings/',,name='view-booking')
    path('browse',views.browse),
    # path('browsedetail',views.browse_with_details),
]