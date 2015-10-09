from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^all/$', 'artical.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'artical.views.article'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'artical.views.language'),
    url(r'^create/$', 'artical.views.create'),
    url(r'^like/(?P<article_id>\d+)/$', 'artical.views.like_article'),
    url(r'^search/$','artical.views.search_title'),
    url(r'^login/$', 'new_pro.views.login'),
    

]