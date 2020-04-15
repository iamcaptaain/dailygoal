from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class ManageUser(BaseUserManager):

    def create_user(self, username , email, password = None , is_active = 'TRUE'):
        if not email:
            raise ValueError("You must have an email Id")
        if not username:
            raise ValueError("Please enter username")
        
        if not password:
            raise ValueError("Please enter password")

        User = self.model(
           email    = self.normalize_email(email),
           username = username,
           is_active = True,
        )
        User.set_password(password)
        User.save(using = self._db)
        return User 
    
    def create_superuser(self, username , email, password = None):
        if not email:
            raise ValueError("You must have an email Id")
        if not username:
            raise ValueError("Please enter username")
        if not password:
            raise ValueError("Please enter password")

        User = self.model(
           email    = self.normalize_email(email),
           username = username,
        )
        User.set_password(password)
        User.is_active = True
        User.is_admin = True
        User.is_staff = True
        User.is_superuser = True
        User.save(using = self._db)
        return User

    def create_staff(self,username, email, password = None):
        if not email:
            raise ValueError("You must have an email Id")
        if not username:
            raise ValueError("Please enter username")
        if not password:
            raise ValueError("Please enter password")
        User = self.model(
           email    = self.normalize_email(email),
           username = username.normalize_username(username),
        )
        User.set_password(password)
        User.is_staff = True
        User.save(using = self._db)
        return User

class User(AbstractBaseUser):
    email           = models.CharField(max_length=99, verbose_name="email", primary_key = True, unique = True)
    username        = models.CharField(max_length=30, unique = True)
    date_join       = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_active       = models.BooleanField(default = False)
    is_staff        = models.BooleanField(default= False)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    # mobile          = models.IntegerField(verbose_name = "Mobile Number", unique=True)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    obb = ManageUser()

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True




class User_Profiles(models.Model):
    Sex_choice = [('ML','MALE',),('FL' ,'FEMALE'), ('TR','TRANSGENDER')]
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=40)
    sex         = models.CharField(max_length=6, choices=Sex_choice)
    mobile      = models.CharField(max_length=10, unique = True, blank = False )
    image       = models.ImageField(upload_to = 'user', blank = True, default = 'user/default.jpg')
    user = models.OneToOneField(User, on_delete=models.PROTECT)


    def __str__(self):
        return self.user.username

    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        User_Profiles.objects.create(user=instance)
    instance.user_profiles.save()   

    

    