from django.urls import path
from . import views
urlpatterns=[
   path('',views.say_hello),
   path('adds',views.add,name='add')
]