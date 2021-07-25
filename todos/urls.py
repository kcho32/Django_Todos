from django.urls import path
from todos import views

app_name = 'todos'

urlpatterns = [
    path('', views.TodoMainView.as_view(), name='index'),#todos/ url polls
    
    path('show_all/', views.AllView.as_view(), name='show_all'),
    
    path('add/', views.Add.as_view(), name='add'),
    path('add/submit_add/', views.add, name='submit_add'),
    
    path('details/', views.DetailList.as_view(), name='details_index'),
    path('details/<int:pk>/', views.DetailedView.as_view(), name='details'),
    
    path('delete/', views.Delete.as_view(), name='delete'),
    path('delete/submit_delete/', views.delete, name='submit_delete'),
    
    path('modify/', views.Modify.as_view(), name='modify'),
    path('modify/modify/', views.modify_1, name='modify_1'),
    path('modify/submit_modify', views.modify_2, name='modify_2'),
    ]