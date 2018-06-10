from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField('用户名', max_length=50)
    display_name = models.CharField('显示名', max_length=200)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.display_name


class Post(models.Model):
    title = models.CharField('标题', max_length=200)
    content = models.TextField('文章')
    post_time = models.DateTimeField('发表时间', auto_now_add=True)
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField('名称', max_length=100)
    slug_name = models.CharField('友好名', max_length=100)

    def __str__(self):
        return self.name
