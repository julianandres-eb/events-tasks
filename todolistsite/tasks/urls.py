from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'create', views.CreateView.as_view(), name='task-create'),
    url(r'update/(?P<pk>[0-9])', views.UpdateView.as_view(), name='task-update'),
    url(r'', views.TaskList.as_view(), name='task-list')
]
