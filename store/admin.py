from django.contrib import admin
from store.models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Cutomer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


# mix profile info user
class ProfileInline(admin.StackedInline):
     model = Profile

#  user Model
class UserAdmin(admin.ModelAdmin):
     model = User
     field = ["username", "first_name", "last_name", "email"]
     inlines = [ProfileInline]
     

# unregister the old way
admin.site.unregister(User)

# re-regiseter the new way
admin.site.register(User, UserAdmin)
     
     






