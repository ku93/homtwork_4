from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите название заголовка",
    )
    content = models.TextField(
        verbose_name="Содержание статьи",
        help_text="Введите текст статьи",
        blank=True,
        null=True,
    )
    preview_image = models.ImageField(upload_to="blog_previews/", blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания поста",
    )
    is_published = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Дата последнего изменения продукта",
    )

    def __str__(self):
        return self.title
