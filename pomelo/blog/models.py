from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.translation import gettext, gettext_lazy


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "Normal"),
        (STATUS_DELETE, "Delete"),
    )
    name = models.CharField(max_length=50, verbose_name=gettext("Name"))
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS,
                                         verbose_name=gettext("STATUS"))
    is_nav = models.BooleanField(default=False, verbose_name=gettext("Set it to nav") + "?")
    owner = models.ForeignKey(User, verbose_name=gettext("Author"))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=gettext("Time of creating"))

    class Meta:
        verbose_name = verbose_name_plural = "Category"

    pass


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, gettext("Normal")),
        (STATUS_DELETE, gettext("Delete")),
    )
    name = models.CharField(max_length=10, verbose_name=gettext("Name"))
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS,
                                         verbose_name=gettext("Status"))
    owner = models.ForeignKey(User, verbose_name=gettext("Author"))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=gettext("Time of creating"))

    class Meta:
        verbose_name = verbose_name_plural = "Tag"
    pass


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, gettext("Normal")),
        (STATUS_DELETE, gettext("Delete")),
        (STATUS_DRAFT, gettext("Draft")),
    )
    title = models.CharField(max_length=255, verbose_name=gettext("Title"))
    desc = models.CharField(max_length=1024, verbose_name=gettext("Desc"))
    content = models.TextField(max_length=2048, verbose_name=gettext("Content"),
                               help_text=gettext("Content")+"---->"+gettext("MarkDown"))
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS,
                                         verbose_name=gettext("Status"))
    category = models.ForeignKey(Category, verbose_name=gettext("Category"))
    tag = models.ManyToManyField(Tag, verbose_name=gettext("Tag"))
    owner = models.ForeignKey(User, verbose_name=gettext("Author"))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=gettext("Time of creating"))

    class Meta:
        verbose_name = verbose_name_plural = "Article"
        ordering = ["-id"]
    pass
