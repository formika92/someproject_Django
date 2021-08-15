from django.db import (
    models,
)

from core.models import (
    BaseCore,
    DataModel,
)


class ProductManager(models.QuerySet):

    def get_queryset(self):
        return super().get_queryset().get_active()

    def get_active(self):
        return self.filter(active=True)

    # def get_slider_trio(self):
    #     return self.order_by('?')[:3]


class Products(BaseCore, DataModel):
    """
    """

    objects = ProductManager.as_manager()
    objects_all = models.Manager()

    category = models.ManyToManyField(
        'Categories',
        verbose_name='category',
        blank=True,
        related_name='products_set',
    )

    manufacture = models.ForeignKey(
        'Manufacturies',
        null=False,
        blank=True,
        related_name='products',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    class Meta:
        db_table = 'products'
        ordering = ('sort', 'title')
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_picture(self):
        for image in self.productpictures_set.all():
            return image


class Categories(BaseCore, DataModel):
    class Meta:
        db_table = 'categories'
        ordering = ('sort', 'title')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class MotherBoardsProduct(Products):
    """
    """
    socket = models.CharField(
        'Сокет',
        max_length=100,
        null=False,
        blank=False,
    )
    chipset = models.CharField(
        'Чипсет',
        max_length=100,
        null=False,
        blank=False,
    )
    frequency_memory = models.SmallIntegerField(
        'Частота памяти',
        null=False,
    )
    num_memory_slots = models.SmallIntegerField(
        'Количество слотов памяти',
        null=False,
    )
    form_factor = models.CharField(
        'Форм-фактор',
        max_length=100,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'motherboards_products'
        ordering = ('sort', 'title')
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'


class ProcessorsProduct(Products):
    """
    """
    core = models.CharField(
        'Ядро',
        max_length=100,
        null=False,
        blank=False,
    )
    socket = models.CharField(
        'Сокет',
        max_length=100,
        null=False,
        blank=False,
    )
    num_cores = models.SmallIntegerField(
        'Количество ядер',
        null=False,
    )
    num_threads = models.SmallIntegerField(
        'Количество потоков',
        null=False,
    )
    frequency = models.SmallIntegerField(
        'Частота',
        null=False,
    )
    lithorgaphy = models.SmallIntegerField(
        'Количество слотов памяти',
        null=False,
    )
    memory_type = models.CharField(
        'Тип памяти',
        max_length=100,
        null=False,
        blank=False,
    )
    graphics_core = models.CharField(
        'Сокет',
        max_length=100,
        null=False,
        blank=False,
    )
    num_memory_channels = models.SmallIntegerField(
        'Количество слотов памяти',
        null=False,
    )
    pci_express_version = models.SmallIntegerField(
        'Версия PCI-Express',
        null=False,
    )
    manufacturer = models.ForeignKey(
        'Manufacturies',
        null=True,
        blank=True,  # что за blank
        related_name='manufacturer_set',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'processors_products'
        ordering = ('sort', 'title')
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'


class Manufacturies(BaseCore, DataModel):
    """

    """
    class Meta:
        db_table = 'manufacturer'
        ordering = ('sort', 'title')
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитель'


class ProductPictures(models.Model):
    """
    """
    image = models.ImageField(
        upload_to='pictures',
    )

    related_obj = models.ForeignKey(
        'products.Products',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='pictures',
    )

    class Meta:
        db_table = 'pictures'
