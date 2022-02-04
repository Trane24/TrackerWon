from django.db import models
from django.urls import reverse


class File(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    context = models.TextField("Описание", max_length=1000)
    photo = models.ImageField("Фото", upload_to="photo/%Y/%m/%d", blank=True)
    file = models.FileField("Фаил", upload_to="file/%Y/%m/%d", blank=True)
    date_published = models.DateTimeField("Дата публикации", auto_now_add=True)
    date_updated = models.DateTimeField("Обновление", auto_now=True)
    is_published = models.BooleanField("Публикация", default=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="file_list",
        verbose_name="Категории",
    )

    def get_absolute_url(self):
        return reverse("file", kwargs={"slug": self.category.slug, "file_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        ordering = ["category"]


class Category(models.Model):
    title = models.CharField("Название категории", max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]
