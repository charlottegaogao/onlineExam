from instantTest.models import Question
from instantTest.models import Choice
from instantTest.models import Point 
from instantTest.models import Test
from instantTest.models import Paper
from django.contrib import admin

<<<<<<< HEAD
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                 ( None,{'fields' : ['question']}),
                 ('Date information', {'fields' : ['pub_date']}),
                 ('Answer', {'fields' : ['answer']}),
                 ('Knowledge points', {'fields' :['point']}),
                ]
    list_display = ('question' , 'pub_date' ,'answer','knowledge_points')
    list_filter = ['pub_date']
    search_fields = ['question']
    inlines = [ChoiceInline]
    
    
class PointAdmin(admin.ModelAdmin):
    fieldsets = [
                 ( 'Content', {'fields' : ['point']}),
                ]

class TestAdmin(admin.ModelAdmin):
    fieldsets = [
                 ( 'Grade', {'fields' : ['grade']}),
                 ( 'Paper', {'fields' : ['paper']}),
                 ( 'Student', {'fields' : ['student']}),     
                ]
    list_display = ('paper' , 'grade' ,'student')
=======


class ChoiceInline(admin.StackedInline):
   model = Choice
   extra = 4


class QuestionAdmin(admin.ModelAdmin):

   fieldsets = [
	   ( None,              {'fields' : ['question']}),
       ('Date information', {'fields' : ['pub_date']}),
       ('Answer',           {'fields' : ['answer']}),
       ('Knowledge points',  {'fields' :['point']}),
   ]
   list_display = ('question' , 'pub_date' ,'answer','knowledge_points')
   list_filter = ['pub_date']
   search_fields = ['question']
   inlines = [ChoiceInline]
class PointAdmin(admin.ModelAdmin):

   fieldsets = [
	   ( 'Content',              {'fields' : ['point']}),
      
   
   ]

class TestAdmin(admin.ModelAdmin):
  

    
  fieldsets = [
    ( 'Grade',              {'fields' : ['grade']}),
    ( 'Paper',              {'fields' : ['paper']}),
    ( 'Student',            {'fields' : ['student']}),     
   
   ]
  list_display = ('paper' , 'grade' ,'student')
>>>>>>> master



class PaperAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id','name')  

admin.site.register(Paper, PaperAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Test,TestAdmin)
=======

  #fieldsets = [
    # {
      #('Paper Name' ,      {'fields' : ['name']}),
      #('Questions'  ,      {'fields' : ['questions']}),

    # }
  #]
  list_display = ('id','name')  
admin.site.register(Paper, PaperAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Test,TestAdmin)
>>>>>>> master
