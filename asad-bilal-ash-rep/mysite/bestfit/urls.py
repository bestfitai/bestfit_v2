from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('profileEdit', views.proifleEdit, name='profileEdit'),
    path('accounts/profile', views.profile, name='profile'),
    path('instructions', views.instructions, name='instructions'),
    path('Test', views.Test, name='sampletest'),
    path('feedback', views.feedback, name='feedback'),
    path('lockscreen', views.lockscreen, name='locked'),
    path('register', views.register, name='register')

]