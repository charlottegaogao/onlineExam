from django.template import Context,loader, RequestContext
from instantTest.models import Question,Test,Paper,Point
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response , get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.views.decorators.cache import never_cache
import random

def signin(request):
    return render_to_response('instantTest/signin.html', context_instance=RequestContext(request))


def index(request):
    paperid = request.GET['paperid']
    username = request.GET['username']
    password = request.GET['password']
    user = auth.authenticate(username=username,password=password)   
    
    if user is not None and user.is_active:
        auth.login(request,user)
        testPaper = get_object_or_404(Paper,pk=paperid)
        if Test.objects.filter(paper=testPaper,student=user):
            return render_to_response('instantTest/signin.html' ,{'error_message':"invalid test",},context_instance=RequestContext(request))
        test = Test(paper=testPaper,grade=0,student=user)
        test.grade = 0
        test.save()
        return render_to_response('instantTest/index.html' ,{'test': test, })
    else:
        return render_to_response('instantTest/signin.html' ,{'error_message':"username or password isn't correct."},context_instance=RequestContext(request))


@never_cache
def details(request,test_id,question_id):    
    test = get_object_or_404(Test,pk=test_id)
    post_question_id = int(question_id)-1
    
    if question_id in request.session:
        return render_to_response('instantTest/signin.html',{'error_message':"invalid operation",},context_instance=RequestContext(request))
    request.session[question_id]='1';
    
    if post_question_id>=0:
        post_question = test.paper.questions.all()[post_question_id]
        random.shuffle(post_question)
        if 'choice' in request.POST:
            if int(post_question.answer) == int(request.POST['choice']):
                test.grade+=1
                test.save()
         
    if len(test.paper.questions.all())>int(question_id):
        question = test.paper.questions.all()[int(question_id)]
        qid = int(question_id)+1
        return render_to_response('instantTest/details.html',{'test':test,'question_id':qid,'question':question,},context_instance=RequestContext(request))
        
    return render_to_response('instantTest/result.html',{'grade':test.grade})


def list_point(request):
    point = Point.objects.all()
    return render_to_response('choosePoint.html',{'point':point}, context_instance=RequestContext(request))


def random_produce(request):
    point_id_list = request.REQUEST.getlist('point')
    num = int(request.POST['num'])
    name = request.POST['name']
    error = ''
    if num > int(len(Question.objects.all())):
        error = 'the datebase cannot satisfy the demands'
    else:
        question_list = []
        for pil in point_id_list:
            pil = Point.objects.get(id = int(pil))
            question_list += Question.objects.filter(point=pil)
        if num > len(question_list):
            error = 'the datebase cannot satisfy the demands' 
        else:
            list(set(question_list))
            index = range(1,len(question_list))
            random_index = random.sample(index, num)
            result = []
            for ri in random_index:
                result.append(question_list[ri])
            newpaper = Paper(name=name)
            newpaper.save()
            newpaper.questions = result
            newpaper.save()
                
    if error == '':
        return render_to_response('result.html',{'result':result})
    else:
        return render_to_response('result.html',{'error':error})    