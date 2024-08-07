from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import FileExtensionValidator

# Create your models here.

class Blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    
    
    class Meta:
        ordering=('-created_on',)

    def comment_count(self):
        return self.comment_set.all().count()   

    def comments(self):
        return self.comment_set.all() 
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile',validators=[FileExtensionValidator(['png','jpg','jpeg'])])

    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE) 
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.TextField(max_length=800)
    comment_time=models.DateTimeField(auto_now_add=True)


    def  __str__(self):
        return self.name.username
    

    




    
