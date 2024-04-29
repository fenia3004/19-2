from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.CharField(
        max_length=100, verbose_name="Описание", help_text="Введите Описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.CharField(
        max_length=100, verbose_name="Описание", help_text="Введите Описание"
    )
    image = models.ImageField(
        upload_to="image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Описание",
        help_text="Введите Описание",
        null=True,
        blank=True,
        related_name='Products',
    )
    price = models.FloatField(verbose_name="Цена за покупку", help_text="Введите цену")
    created_at = models.DateField(
        blank=True, null=True, verbose_name="Дата создании записи"
    )
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Дата последнего изменения записи"
    )

    class Meta:
        verbose_name = "Наименование"
        verbose_name_plural = "Наименования"
        ordering = ["category", "price", "name"]

    def __str__(self):
        return self.name
