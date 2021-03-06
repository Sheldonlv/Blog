from django.contrib import admin
from .models import essay_data,para_data,article_data

class essayAdmin(admin.ModelAdmin):
    list_display = ('Num', 'pub_time',)

class paraAdmin(admin.ModelAdmin):
    list_display = ('Num', 'title','pub_time',)

admin.site.register(essay_data,essayAdmin)
admin.site.register(para_data,paraAdmin)
admin.site.register(article_data)
# Register your models here.
