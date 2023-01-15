from django.db import models

# Create your models here.
# Tag and Task models
class Tag(models.Model):
        # Setting `unique=True` on the name attribute below ensures that no two tags
        # will have the same name
    name = models.CharField(max_length=30, unique=True)
        # When we add the `tags` ManyToMany field to the Task model below,
        # Django automatically creates an attribute `task_set` on the Tag Model
        # so that we can use the relationship between Tags and Tasks both ways

class Task(models.Model):
       
    description = models.CharField(max_length=255)
        # The `tags` field connects the `Tag` model to the `Task` model, automatically
        # creating a junction `task_tags` table in the database for us when migrated
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    task = models.ForeignKey(Task, on_delete = models.CASCADE)