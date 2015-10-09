from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from .models import Artical,Comment
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import ArticleForm
from django.utils import timezone
# Create your views here.

def hello(request):
	name = "Mohit"
	html = "<html><body>Hi %s, This seems to have worked!</body></html>" % name
	return HttpResponse(html)

def hello_template(request):
	name = "Mohit"
	t = get_template('hello.html')
	html = t.render(Context({'name': name}))
	return HttpResponse(html)

def hello_template_simple(request):
	name = "Mohit"
	return render_to_response('hello.html',{'name':name})

class HelloTemplate(TemplateView):
	template_name = 'hello_class.html'

	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'Mohit'
		return context

def articles(request):
	language = 'en-gb'
	session_language = 'en-gb'
	current_year = timezone.now().year
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']

	return render_to_response('articles.html',{'articles':Artical.objects.all(),'cust':Artical.objects.order_by('-pub_date')[:5],'spl_article':Artical.objects.get(id=4) ,'language':language, 'session_language': session_language })


def article(request,article_id=2):
	return render_to_response('article.html',{'article':Artical.objects.get(id=article_id),'articles':Artical.objects.all(),'comments':Comment.objects.all()})

def language(request, language='en-gb'):
	response = HttpResponse('setting language to %s' % language)

	response.set_cookie('lang', language)

	response.session['lang'] = language

	return response

def create(request):
	if request.user.is_authenticated():
		if request.POST:
			form = ArticleForm(request.POST,request.FILES)
			if form.is_valid():
				form.save()

				return HttpResponseRedirect('/articles/all')
		else:
			form = ArticleForm()

		args ={}
		args.update(csrf(request))

		args['form'] = form

		return render_to_response('create_article.html',args)
	else:
    		#return render_to_response('/accounts/login.html',{})
    		c={}
    		c.update(csrf(request))
    		return render_to_response('login.html',c)

def like_article(request, article_id):
	if request.user.is_authenticated():
		if article_id:
			a = Artical.objects.get(id=article_id)
			count = a.likes
			count +=1
			a.likes = count
			a.save()

			return HttpResponseRedirect('/articles/get/%s' % article_id)
        
    	else:
    		#return render_to_response('/accounts/login.html',{})
    		c={}
    		c.update(csrf(request))
    		return render_to_response('login.html',c)

	 

def search_title(request):
	if request.method == 'GET':
		search_text = request.GET['search_text']
	else:
		search_text = ''

	articles = Artical.objects.filter(title__contains=search_text)

	return render_to_response('ajax_search.html',{'articles':articles})
