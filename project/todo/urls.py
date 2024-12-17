from django.urls import path
from . import views

urlpatterns = [
    path('todo/',view=views.TodoList.as_view(),name='todo'),
    path('todo/create/',view=views.TodoCreate.as_view(),name='todo-create'),
    path('todo/filter-by-status/',view=views.TodoFilterByStatus.as_view(),name='todo-filter-by-status'),
    path('todo/<id>/',view=views.TodoDetail.as_view(),name='todo'),
    path('todo/edit/<id>/',view=views.TodoEdit.as_view(),name='todo-edit'),
    path('todo/delete/<id>/',view=views.TodoDelete.as_view(),name='todo-delete'),
    path('todo/completed/<id>/',view=views.TodoComplete.as_view(),name='todo-complete'),
]