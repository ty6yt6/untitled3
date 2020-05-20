from django.contrib import admin

# Register your models here.
from .models import *
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id","btitle","bread","bcomment"]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id","hbook","hname","hgender","hcomment"]
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)