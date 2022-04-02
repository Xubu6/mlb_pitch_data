from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_data, name='all_data'),
    path('<int:page_num>/', views.all_data_detail, name='all_data_detail'),
    path('atbats/', views.atbats, name='atbats'),
    path('atbats/<int:page_num>/', views.atbats_detail, name='atbats_detail'),
    path('pitches/', views.pitches, name='pitches'),
    path('pitches/<int:page_num>/', views.pitches_detail, name='pitches_detail'),
]