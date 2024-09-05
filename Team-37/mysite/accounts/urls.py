from django.urls import path
from . import views
urlpatterns=[
 path('game/',views.snakeform,name='snakeform'),
 path('',views.login_page,name='login'),
 path('register/',views.register_page,name='register'),
 path('logout/',views.logoutuser,name='logout'),
 path('home/',views.home_page,name='home'),
 path('woardgame/',views.word_page,name='word'),
 path('cardgame/',views.card_page,name='card'),
 path('dashboard/',views.dashboard_page,name='dashboard'),
 path('delete/<str:pk>',views.delete_order,name='delete')
]