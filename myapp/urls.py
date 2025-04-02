from django.urls import path
from .views import findbus  # ✅ Import the view

urlpatterns = [
    path('findbus/', findbus, name='findbus'),  # ✅ Define the URL pattern
]
