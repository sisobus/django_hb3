from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('', views.index, name='index'),
    path('', views.UserList.as_view(), name='user list'),
    path('<int:pk>/', views.UserItem.as_view(), name='user item'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('this/', views.user_information, name='this_user_information'),
]


