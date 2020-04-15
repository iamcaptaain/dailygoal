from django.db import models
from accounts.models import User
# Create your models here.

class UserActivity(models.Model):
    user            = models.ForeignKey(User,on_delete=models.PROTECT)
    activity        = models.CharField(max_length = 20, blank = False, )
    description     = models.TextField(max_length = 100, blank = True)
    time            = models.TimeField()
    duration        = models.CharField(max_length = 3, blank = False)
    uploadtime      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity

    class Meta:
        db_table = "UserActivity"

class UserNotes(models.Model):
    user    = models.ForeignKey(User, on_delete= models.PROTECT)
    notes   = models.TextField()
    star    = models.BooleanField(default=False)
    waqt    = models.DateTimeField(auto_now_add=True)
    # lisst   = models.
    def __str__(self):
        return self.user.username   
    
    class Meta:
        db_table = "UserNotes"