from django.conf.urls import include, url
urlpatterns = [
    url(r'^all/$', 'blog.views.blogs'),
    url(r'^get/(?P<blog_id>\d+)/$', 'blog.views.blog'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'blog.views.language'),
    
]


