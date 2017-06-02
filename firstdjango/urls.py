# In firstdjango/urls.py

from django.conf.urls import include, url
from django.contrib import admin

from inventory import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'firstdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #This url applies index() created in views to the homepage (ie: base url)
    url(r'^$', views.index, name='index'),

    #This url has a regex that declares id as a tag that it can use for processes
    #it tags item/'digits' with the item_detail method created in views
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),

    url(r'^admin/', include(admin.site.urls)),
]
