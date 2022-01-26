from django.db import models


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        ordering = ["category"]


class Category(models.Model):
    title = models.CharField("Название категории", max_length=50)
    general_category = models.ForeignKey(
        "GeneralCategory",
        on_delete=models.PROTECT,
        related_name="category_list",
        verbose_name="Главные категории",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["general_category"]


class GeneralCategory(models.Model):
    title = models.CharField("Главная категория", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Главная категория"
        verbose_name_plural = "Главные категории"
        ordering = ["title"]
