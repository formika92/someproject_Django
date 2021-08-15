from django.db import (
    models,
)
from django.urls import (
    reverse,
)


class DataModel(models.Model):
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        blank=False,
    )
    last_modified = models.DateTimeField(
        verbose_name='Дата модификации',
        auto_now=True,
        blank=True,
    )

    # last_editor_id = models.ForeignKey(UsersProfile)

    class Meta:
        abstract = True


class BaseCore(models.Model):
    """

    """
    title = models.CharField(
        'заголовок объекта',
        max_length=250,
        blank=True,
        null=True,
    )

    description = models.TextField(
        'описание объекта',
        blank=True,
        null=True,
    )
    sort = models.IntegerField(
        'номер объекта для сортировки',
        default=0,
        blank=True,
        null=False,
    )
    active = models.BooleanField(
        'Активен ли объект',
        default=True,
        db_index=True,
    )

    class Meta:
        ordering = ('sort', 'title')
        abstract = True

    def __str__(self):
        return f'{self.title}' if self.title else ''

    def delete(self, **kwargs):
        if 'force' in kwargs:
            super().delete()
        else:
            self.active = False
            self.save()

    @classmethod
    def get_model_name(cls):
        return cls.__name__.lower()

    @classmethod
    def get_app_name(cls):
        return cls._meta.app_label.lower()

    def get_absolute_url(self):
        return reverse(
            f'{self.get_app_name()}:{self.get_model_name().capitalize()}Detail',
            args=[self.pk],
        )


# class BaseOrders(models.Model):
#     """
#     """
#
#     class Meta:
#         abstract = True
