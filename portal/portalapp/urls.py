from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^login/$', auth_views.login),
    url(r'^users/(?P<username>[\w.@+-]+)/$',views.displaypoints,name = 'displaypoints'),
    url(r'^users/$',views.displayusers,name = 'displayusers'),
    # url(r'^users/(?P<user_id>[0-9]+)/$',views.displaypoints,name = 'displaypoints')
]