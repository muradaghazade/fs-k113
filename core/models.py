from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', related_name='posts')
    # user

class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    
class Tag(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', related_name='recipes', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', related_name='recipes')


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    # user