from django.urls import path
from app.views import home ,login,signup,signout,add_todo,delete_todo,change_todo


urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/' , signout ), 
    path('add-todo/',add_todo),
    path('delete-todo/<int:id>' , delete_todo ), 
     path('change-status/<int:id>/<str:status>' , change_todo ), 
]
