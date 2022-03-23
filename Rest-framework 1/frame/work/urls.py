from django.urls import path,include
from.views import inner,index,create,edit,delete,Update,login,user_logout,home
urlpatterns=[
    path('car/',inner),
    path('index/',index),
    path('create/',create),
    path('edit/<str:name>/',edit),
    path('delete/<str:name>/',delete),
    path('Update/<str:name>/',Update),
    path('login/',login),
    path('logout/',user_logout),
    path('home/',home),
]