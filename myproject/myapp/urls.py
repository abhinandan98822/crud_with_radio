from django.urls import path
from . import views

urlpatterns = [
    path('register',views.Register,name='Register'),
    # path('login',views.Login,name='Login'),
    path('table',views.Table,name='table'),
    path('delete/<int:id>',views.Delete,name='delete'),
    path('edit/<int:id>',views.Edit,name='edit')
]