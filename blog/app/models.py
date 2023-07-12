from django.contrib.auth.models import User
from django.db import models


class BlogModel(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)

    class Meta:
        abstract = True


class Article(BlogModel):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['created_at']


def cal_key(article):
    present_keys = Comment.objects.filter(article=article).order_by('-key').values_list('key', flat=True)
    if present_keys:
        return present_keys[0] + 1
    else:
        return 1


class Comment(BlogModel):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    key = models.PositiveIntegerField(null=False)

    class Meta:
        unique_together = ('key', 'article')

    def save(self, *args, **kwargs):
        key = cal_key(self.article)
        self.key = key
        super(Comment, self).save(*args, **kwargs)
