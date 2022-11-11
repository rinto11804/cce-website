from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about_page, name='about'),
    path('academics', views.academics_page, name='academics'),
    path('admission', views.admission_page, name='admission'),
    path('arts', views.arts_page, name='arts'),
    path('governing_body', views.governing_body__page, name='governingBody'),
    path('campuslife', views.campuslife_page, name='campuslife'),
    path('management', views.management_page, name='management'),
    path('nirf', views.nirf_page, name='nirf'),
    path('iqac', views.iqac_page, name='alumini'),
    path('alumini', views.alumini_page, name='iqac'),
    path('gallery', views.gallery_page, name='gallery'),
    path('test', views.test_page, name='Department of ECE'),

]

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
