from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
)
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
)

from .models import (
    Products,
)


class ProductList(ListView):
    """
    """
    model = Products

    # TODO дописать с формами

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ProductsDetail(DetailView):
    model = Products


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    """
    """
    model = Products
    # TODO дописать с формами
