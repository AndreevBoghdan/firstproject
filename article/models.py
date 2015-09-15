from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Article(models.Model):
	class Meta():
		db_table = 'article'
	article_title=models.CharField(max_length = 200)
	article_text=models.TextField()
	article_date=models.DateTimeField()
	article_likes=models.IntegerField(default=0)

	def was_published_recently(self):
    		now = timezone.now()
    		return now - datetime.timedelta(days=1) <= self.article_date <= now
 

class Comments(models.Model):
	class Meta():
		db_table = 'comments'

	comments_text = models.TextField("New Comment")
	
	comments_article = models.ForeignKey(Article)
	comments_user = models.ForeignKey(User, null=True)


