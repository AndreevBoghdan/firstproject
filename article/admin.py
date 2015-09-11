from django.contrib import admin
from article.models import Article, Comments


# Register your models here.
#class ArticleInline(admin.StackedInline):
#	model = Comments
#	extra = 0

class ArticleAdmin(admin.ModelAdmin):
	fields=['article_title', 'article_text', 'article_date']
#	inlines=[ArticleInline]
	list_filter = ['article_date']
	list_display = ('article_title', 'article_date')
	search_fields = ['article_title']


admin.site.register(Article,ArticleAdmin)