from django.db import models


class File(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    context = models.TextField("Описание", max_length=1000)
    photo = models.ImageField("Фото", upload_to="photo/%Y/%m/%d", blank=True)
    file = models.FileField("Фаил", upload_to="file/%Y/%m/%d", blank=True)
    date_published = models.DateTimeField("Дата публикации", auto_now_add=True)
    date_updated = models.DateTimeField("Обновление", auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="file_list")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"


class Category(models.Model):
    title = models.CharField("Название категории", max_length=50)
    general_category = models.ForeignKey("GeneralCategory", on_delete=models.PROTECT, related_name="category_list")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class GeneralCategory(models.Model):
    title = models.CharField("Главная категория", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Главная категория"
        verbose_name_plural = "Главные категории"
