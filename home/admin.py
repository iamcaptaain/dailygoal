from django.contrib import admin
from .models import UserActivity, UserNotes
# Register your models here.




# class ActivityCreation(models)
class AdminUserActivity(admin.ModelAdmin):
    list_display = ['user','activity', 'description', 'time', 'duration', 'uploadtime']
    fieldsets = (
        (None, {'fields': ('user','activity','description')}),
        ('time', {'fields': ('time','duration')}),
    )

class AdminNotes(admin.ModelAdmin):
    list_display = ['star','user','notes','waqt']
    fieldsets = (
        (None, {'fields': ('user','star','notes')}),
    )



admin.site.register(UserActivity,AdminUserActivity)
admin.site.register(UserNotes,AdminNotes)