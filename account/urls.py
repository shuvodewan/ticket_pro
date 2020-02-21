from django.urls import path,include

from . import  views
#load media file
from django.conf import settings
from django.conf.urls.static import static

app_name="account"
urlpatterns = [
    path('add_user/',views.UserCreate,name='add_user'),
    path('user_list/',views.list_user,name='user_list'),
    path('update_user/<int:pk>',views.update_user,name='update_user'),
    path('delete_user/<int:pk>',views.delete_user,name="delete_user"),
    path('member_list/',views.member_list,name="member_list"),
]
