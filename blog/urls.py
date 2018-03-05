from django.conf.urls import url 

from blog import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$',views.post_model_detail_view,name='detail'),
    url(r'^$',views.post_model_list_view,name='list'),
    url(r'^create/$',views.post_model_create_view,name='create'),
    url(r'^(?P<id>\d+)/edit/$',views.post_model_update_view,name='update'),
    url(r'^(?P<id>\d+)/delete/$',views.post_model_delete_view,name='delete'),
]