from django.urls import path
from . import views


urlpatterns=[
    path('',views.todo,name="todo"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('updatetodo/<int:id>/',views.update,name='update'),
]


# /<int:id>/
# to know which id is deleted