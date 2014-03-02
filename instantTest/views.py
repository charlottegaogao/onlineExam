from django.template import Context,loader, RequestContext
from instantTest.models import Question,Test,Paper
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response , get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.views.decorators.cache import never_cache 

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
        if 'choice' in request.POST:
            if int(post_question.answer) == int(request.POST['choice']):
                test.grade+=1
                test.save()
         
    if len(test.paper.questions.all())>int(question_id):
        question = test.paper.questions.all()[int(question_id)]
        qid = int(question_id)+1
        return render_to_response('instantTest/details.html',{'test':test,'question_id':qid,'question':question,},context_instance=RequestContext(request))
        
    return render_to_response('instantTest/result.html',{'grade':test.grade},)

    
