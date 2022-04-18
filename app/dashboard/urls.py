from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('*', views.home, name='home_wildcard'),
    path('all/', views.all_data, name='all_data'),
    path('all/<int:page_num>/', views.all_data_detail, name='all_data_detail'),
    path('atbats/', views.atbats, name='atbats'),
    path('atbats/<int:page_num>/', views.atbats_detail, name='atbats_detail'),
    path('pitches/', views.pitches, name='pitches'),
    path('pitches/<int:page_num>/', views.pitches_detail, name='pitches_detail'),
    path('stats/', views.stats, name='stats'),
    path('stats/<str:sp_name>/', views.sp, name='sp'),
    path('stats/<str:sp_name>/<int:page_num>/', views.sp_detail, name='sp_detail'),
]