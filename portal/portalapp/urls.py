from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<username>[\w.@+-]+)/$',views.displaypoints,name = 'displaypoints'),
    # url(r'^users/$',views.displayusers,name = 'displayusers'),        url(r'^registration/passwordreset.html/$',views.passwordreset,name='passwordreset'),
    url(r'^portalapp/logissue/$',views.logissue,name='logissue'),
    url(r'^portalapp/report/$',views.report,name='report'),
    url(r'^portalapp/uploadhandle/$',views.uploadhandle,name='uploadhandle'),
    url(r'^registration/passwordreset.html/$',views.passwordreset,name='passwordreset'),
   # url(r'^password/$', views.change_password, name='change_password'),
    # url(r'^users/(?P<user_id>[0-9]+)/$',views.displaypoints,name = 'displaypoints')
]

urlpatterns += staticfiles_urlpatterns()