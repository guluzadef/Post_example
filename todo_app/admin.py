from django.contrib import admin
from .models import *
admin.site.register(Main_title)
admin.site.register(Menu)
admin.site.register(TXT)
admin.site.register(Main)
admin.site.register(icon)
admin.site.register(Contact)
admin.site.register(Contact_me)
admin.site.register(Register_User)
admin.site.register(Login_User)
admin.site.register(Article)
admin.site.register(PostPage)
admin.site.register(Profil)
admin.site.register(UpdatePage)

@admin.register(About_Me)
class About_me_admin(admin.ModelAdmin):
    list_display = ["title"]



# Register your models here.

