from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Endpoint to obtain an auth token
    path('token/', obtain_auth_token, name='api_token_auth'),

    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('users/<str:email>/', views.UserDetail.as_view(), name='user-detail'),
]

