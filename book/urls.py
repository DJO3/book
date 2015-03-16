from django.conf.urls import patterns, include, url
from django.contrib import admin
from index.views import IndexView
from library import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^book', views.book, name='book'),
    url(r'^add_book', views.add_book, name='add_book'),
    url(r'^$', IndexView.as_view(), name='index'),
)
