from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('BSH/', views.depHome, name='BSH'),
    path('BSH/<str:route>', views.BSH, name='BSH'),
]


if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
