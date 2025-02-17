from django.db import models
from django.utils import timezone
from datetime import datetime

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="category/photo",
        blank=True,
        null=True,
        verbose_name="Фотография продукта",
        help_text="Загрузите фотографию продукта",
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    picture = models.ImageField(
        upload_to="product/picture",
        blank=True,
        null=True,
        verbose_name="Фотография продукта",
        help_text="Загрузите фотографию продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию продукта",
        blank=True,
        null=True,
        related_name='products'
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена покупки",
        help_text="Введите цену покупки продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания продукта",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Дата последнего изменения продукта",
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(User, verbose_name="Владелец", help_text='Владелец продукта', blank=True, null=True, on_delete=models.SET_NULL)



    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ("can_unpublish_product", "can unpublish product"),
            ("can_delete_product", "can delete product"),
        ]

    def __str__(self):
        return self.name
