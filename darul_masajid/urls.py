"""darul_masajid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from reciters import views

router=DefaultRouter()
router.register("surah",views.SurahAPIView,basename="surah")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("profile/<int:pk>",views.RecitersProfileAPIView.as_view()),
    path("profile/",views.RecitersProfileAPIView.as_view()),
    path("reciterslist/",views.RecitersListWithImageAPIView.as_view()),
    path("",include(router.urls)),
    path("fun/",views.fun),
    # path("surah/<int:pk>",views.SurahAPIView.as_view()),
   
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

