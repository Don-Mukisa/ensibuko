from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_requisition, requisition_list, signup,login_view,delete_requisition

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
    path('',login_view,name='login'),
    path('create/', create_requisition, name='create_requisition'),
    path('list/', requisition_list, name='requisition_list'),
    path('login/', login_view,name='login'),
    path('delete_requisition/<int:requisition_id>/', delete_requisition, name='delete_requisition'),
 # Add more views as needed
]
