from django.urls import path
from .views import *

app_name = 'utilisateurs'

urlpatterns = [
    path('login', login_users , name='login_users'),
    path('logout_users', logout_users , name='logout_users'),
    path('singup', sing_up , name='sing_up'),
    path('update_user/<int:id>/', update_user , name='update_user'),
    path('delete_user/<int:id>/', delete_user , name='delete_user'),
    path('update_user_value/<int:id>/', update_user , name='update_user'),
    path('viewreservation/<int:id>/', viewreservation, name='viewreservation'),
    path('reservation/<int:id_chambre>/<int:user_id>', reservation , name='reservation'),
]