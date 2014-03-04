from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Point(models.Model):
    point = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.point

        
class Question(models.Model):
<<<<<<< HEAD
    # int
    choice1 = 0
    choice2 = 1
    choice3 = 2
    choice4 = 3
    ANSWER_CHOICE = (
                     (choice1, 'Choice1'),
                     (choice2, 'Choice2'),
                     (choice3, 'Choice3'),
                     (choice4, 'Choice4'),
                     )
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer = models.IntegerField(default=0, choices=ANSWER_CHOICE)
=======
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer = models.IntegerField(default=0)
>>>>>>> master
    point = models.ManyToManyField(Point)
    def __unicode__(self):
        return self.question
    def knowledge_points(self):
        return ', '.join([a.point for a in self.point.all()])
    knowledge_points.short_description = "Knowledge Point"

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length = 200)
    def __unicode__(self):
<<<<<<< HEAD
        return self.choice
=======
       return self.choice
>>>>>>> master

class Paper(models.Model):
    questions = models.ManyToManyField(Question)
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

class Test(models.Model):
    paper = models.ForeignKey(Paper)
    grade = models.IntegerField(default = 0)
    student = models.ForeignKey(User)
    def __studentName(self):
        return student.username
    #dueDate =models.DateTimeField('date overdue')
    def __unicode__(self):
        return self.paper.name
<<<<<<< HEAD
=======



>>>>>>> master
