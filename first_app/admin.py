from django.contrib import admin
from .models import Question,AccessRecords,WebPage,Topic
# Register your models here.
admin.site.register(Question)
admin.site.register(WebPage)
admin.site.register(AccessRecords)
admin.site.register(Topic)