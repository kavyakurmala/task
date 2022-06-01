from django.urls import path
from app1.views import delete_data, update

app_name = 'app1'

urlpatterns = [
    path('delete/<int:pk>/',delete_data,name='deltedata'),
    path('<int:pk>/',update,name='up')

]