from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='instances'),
    path('start', views.create, name='start'),
    path('<name>/', views.instance, name='instance'),
    path('<name>/start', views.start, name='start'),
    path('<name>/stop', views.stop, name='stop'),
    path('<name>/delete', views.delete, name='delete'),
    path('<name>/stderr', views.stderr, name='stderr'),
    path('<name>/stdout', views.stdout, name='stdout'),
]