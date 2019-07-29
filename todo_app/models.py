from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
class Main_title(models.Model):
    sitename = models.CharField(max_length=255)
    mainname = models.CharField(max_length=250)
    footername = models.CharField(max_length=250)


class Menu(models.Model):
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250, null=True, blank=True)


class Main(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to="photos")


class TXT(models.Model):
    texth1 = models.CharField(max_length=255)
    texth3 = models.CharField(max_length=255)
    bytextwhen = models.DateTimeField(max_length=255, default=timezone.now)
    by = models.CharField(max_length=255)

    url = models.CharField(max_length=250)


class icon(models.Model):
    icon = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return f"{self.icon}"


class About_Me(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to="about_photo")
    text = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Contact_me(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    text = models.TextField()

    img = models.ImageField(upload_to="contact_photo")

    def __str__(self):
        return f"{self.title}"


class Register_User(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to="about_photo")
    text = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Login_User(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to="about_photo")
    text = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Profil(models.Model):
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profil_photo", null=True, blank=True)
    background_image = models.ImageField(upload_to="profil_photo", null=True, blank=True )
    about = models.CharField(max_length=400)

    def get_background_image(self):
        if self.background_image:
            return self.background_image.url
        else:
            return ""

    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return ""





class Article(models.Model):
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="post")
    content = RichTextField()
    date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    class Meta:
        ordering=["-id"]

class PostPage(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image=models.ImageField(upload_to="postpage")

class UpdatePage(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="update")

class UserSetting(models.Model):
    name=models.CharField(max_length=250)
    surname=models.CharField(max_length=250)
    img=models.ImageField()
    email=models.EmailField()


    def __str__(self):
        return f"{self.name}"