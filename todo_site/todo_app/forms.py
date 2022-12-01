from django.forms import ModelForm

from todo_app.models import Task, Comment


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)

        #self.instance is the comment we are creating with this form
        self.instance.task = task




        #the form will get created with a task, we need to pull that task out and keep track of it