import os
from django.urls import (
    path,
)
from .views import (
    ProductList,
    ProductsDetail,
    ProductUpdate,
)

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('<int:pk>/edit/', ProductUpdate.as_view(), name='ProductUpdate'),
    path('<int:pk>/', ProductsDetail.as_view(), name='ProductsDetail'),
    path('', ProductList.as_view(), name='all'),
]
