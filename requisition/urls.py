from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_requisition, requisition_list, signup,login_view

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('',login_view,name='login'),
    path('create/', create_requisition, name='create_requisition'),
    path('list/', requisition_list, name='requisition_list'),
    path('login/', login_view,name='login'),
    # Add more views as needed
]
