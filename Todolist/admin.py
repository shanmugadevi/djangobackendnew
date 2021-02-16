from django.contrib import admin

# Register your models here.
from .models import Todo


class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description')  # add this


admin.site.register(Todo, TodoAdmin)  # add this
