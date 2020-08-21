from django.contrib import admin
from .models import Question,Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Admin"
admin.site.index_title = "Pollster Admin"


admin.site.register(Question)
admin.site.register(Choice)