from django.db import models
from django.utils.timezone import now
from django.contrib. auth.  models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    views= models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)
    content = RichTextField()
    post_image = models.ImageField(upload_to="static",default="")

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()  # Corrected field name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
