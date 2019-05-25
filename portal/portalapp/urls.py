from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

### FLOW
## url is entered -> matches url -> goes into views calls  a function -> Function does some computation -> Renders a new page
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<username>[\w.@+-]+)/$',views.displaypoints,name = 'displaypoints'),
    url(r'^portalapp/logissue/$',views.logissue,name='logissue'),
    url(r'^portalapp/report/$',views.report,name='report'),
    url(r'^portalapp/uploadhandle/$',views.uploadhandle,name='uploadhandle'),
    url(r'^registration/passwordreset.html/$',views.passwordreset,name='passwordreset'),
]

urlpatterns += staticfiles_urlpatterns()