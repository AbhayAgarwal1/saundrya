from django.conf.urls import url
from beautician import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^register/$',views.UserFormView,name='register'),
]
