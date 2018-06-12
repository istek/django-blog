from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.


class User(models.Model):
    username = models.CharField('用户名', max_length=50)
    display_name = models.CharField('显示名', max_length=200)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.display_name

    class Meta:
        db_table = 'user'
        default_related_name = 'user'
        ordering = ['username']
        verbose_name = "user"
        verbose_name_plural = "user"


class Post(models.Model):
    title = models.CharField('标题', max_length=200)
    content = MarkdownxField()
    post_time = models.DateTimeField('发表时间', auto_now_add=True)
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', blank=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        default_related_name = 'post'
        ordering = ['-post_time']
        verbose_name = "post"
        verbose_name_plural = "post"


class Tag(models.Model):
    name = models.CharField('名称', max_length=100)
    slug_name = models.CharField('友好名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'
        default_related_name = 'tag'
        ordering = ['slug_name']
        verbose_name = "tag"
        verbose_name_plural = "tag"
