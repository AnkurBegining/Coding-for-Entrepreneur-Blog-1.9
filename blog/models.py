from django.db import models

# Create your models here.
# MVC model followed

class post(models.Model):
    title = models.CharField(max_length=150)
    image = models.FileField(null= True, blank= True)
    post_content =  models.TextField()
    updated = models.DateTimeField(auto_now= True, auto_now_add= False)
    timestamp = models.DateTimeField(auto_now= False, auto_now_add= True)

    def __str__(self):
        return self.title


    class Meta:
        ordering =['-timestamp', '-updated']