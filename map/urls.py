"""utopia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

# DEBUG:
from django.conf import settings
from django.conf.urls.static import static

app_name = 'map'

urlpatterns = [
    path('', views.map, name='map'),
    path('event/<int:event>', views.map, name='map'),
    path('people/<int:people>', views.map, name='map'),
    path('place/<int:place>', views.map, name='map'),
    path('profile/<str:profilename>', views.profile, name="profile"),
    path('settings/', views.settings, name="settings"),
    path('register/', views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("api/", views.api_request, name="api"),
]
# DEBUG:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
