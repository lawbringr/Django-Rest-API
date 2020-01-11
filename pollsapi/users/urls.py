from django.urls import path, re_path
from users import apiviews
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', apiviews.UserList.as_view()),
    path('users/<int:pk>/', apiviews.UserDetail.as_view()),
]






# router = DefaultRouter()
# router.register('api/users/', UserViewSet, basename='users')

# urlpatterns = [
#     re_path(r'^users/$', apiviews.user_list),
#     re_path(r'^users/(?P<pk>[0-9]+)$', apiviews.user_detail),
# ]

# urlpatterns += router.urls