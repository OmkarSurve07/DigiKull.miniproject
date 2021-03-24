from django.contrib import admin
from .models import blog, author, entry

# Register your models here.
admin.site.register(blog)
admin.site.register(author)
admin.site.register(entry)