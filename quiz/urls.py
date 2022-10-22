from django.urls import path
from . import views
from .views import home,signup,quizee, addQuestion, ProfileDetail

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('result',views.result,name='result'),
    path('quizee',views.quizee,name='quizee'),
    path('addquestion',views.addquestion,name='addquestion'),
    path('index',ProfileDetail.as_view(), name='ProfileDetail'),
    path('update', views.addQuestion, name='addquestion'),
]