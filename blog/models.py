from django.db import models

# Create your models here.
# MVC model followed


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_location,
                              null= True,
                              blank= True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    post_content =  models.TextField()
    updated = models.DateTimeField(auto_now= True, auto_now_add= False)
    timestamp = models.DateTimeField(auto_now= False, auto_now_add= True)

    def __str__(self):
        return self.title


    class Meta:
        ordering =['-timestamp', '-updated']