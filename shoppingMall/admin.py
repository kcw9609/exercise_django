from django.contrib import admin
from .models import Post, Category, Tag, Manufacturer
# Register your models here.
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)




class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Manufacturer, ManufacturerAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}#초기값주는거
admin.site.register(Tag, TagAdmin)
