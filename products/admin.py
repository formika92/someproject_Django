from django.contrib import (
    admin,
)

from .models import (
    Categories,
    Manufacturies,
    ProcessorsProduct,
    ProductPictures,
    MotherBoardsProduct,

)


class PicturesInline(admin.TabularInline):
    fk_name = 'related_obj'
    model = ProductPictures


@admin.register(MotherBoardsProduct)
class MotherBoardsProductAdmin(admin.ModelAdmin):
    inlines = [PicturesInline, ]


@admin.register(ProcessorsProduct)
class MotherBoardsProductAdmin(admin.ModelAdmin):
    inlines = [PicturesInline, ]


admin.site.register(
    Manufacturies,
)


admin.site.register(
    Categories,
)

