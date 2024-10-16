# project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import ReviewViewSet, UserViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'users', UserViewSet, basename='user')

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel path
    path('api/', include(router.urls)),  # Include the router URLs under the 'api/' path
    path('api/', include('reviews.urls')),  # Include the reviews app URLs under the 'api/' path
]
