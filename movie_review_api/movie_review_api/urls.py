# movie_review_api/urls.py

from django.contrib import admin
from django.urls import path, include
from reviews import views  # Import the views from the reviews app

urlpatterns = [
    path('admin/', admin.site.urls),  # Make sure this is defined only once
    path('', views.home, name='home'),  # Use the home view from reviews.views
    path('api/', include('reviews.urls')),  # Include API routes from the reviews app
]
