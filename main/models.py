from django.db import models


class ListFiles(models.Model):
    title = models.CharField(max_length=50, )
    context = models.TextField(max_length=1000)
    photo = models.ImageField()
    file = models.FileField()
    date_published = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    categoryLists = models.ForeignKey("CategoryLists", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"


class CategoryLists(models.Model):
    title_CategoryLists = models.CharField(max_length=50, )
    categoryLists = models.ForeignKey("CategoryGeneral", on_delete=models.PROTECT)

    def __str__(self):
        return self.title_CategoryLists

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class CategoryGeneral(models.Model):
    title_CategoryGeneral = models.CharField(max_length=50, )

    def __str__(self):
        return self.title_CategoryGeneral

    class Meta:
        verbose_name = "Category - general"
        verbose_name_plural = "Categories - general"
