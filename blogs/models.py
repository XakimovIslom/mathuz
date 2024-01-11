from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=121)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=121)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=121)
    content = models.TextField()
    tag = models.ManyToManyField(Tag, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        ordering = ['id']
