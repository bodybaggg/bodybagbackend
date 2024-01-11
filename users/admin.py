from django.contrib import admin
from . models import User,CategoryName

class BodyBagAdmin(admin.ModelAdmin):
    list_display =('id','name','gender','email','phone_number','instagram','location','category','experience','unique_code','is_staff','is_superuser','is_active')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 10
    list_editable = ("is_staff","is_active",)
    

# Register your models here.
admin.site.register(User,BodyBagAdmin)
admin.site.register(CategoryName)