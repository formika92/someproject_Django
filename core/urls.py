import os
from django.urls import path, re_path
from .views import (
    Index,
)

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    re_path('', Index.as_view(), name='index'),
]