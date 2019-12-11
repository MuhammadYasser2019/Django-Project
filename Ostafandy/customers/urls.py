from django.urls import path
from customers import views

urlpatterns = [
    path('signup_user', views.signup),
    path('signup_osta', views.signup_ostafandy),
    path('login/<str:username>/<str:password>/', views.login),
    path('list/<int:cid>/', views.list_osta),
    path('list/', views.list_osta_all),
    path('list_all/', views.list_all),

]