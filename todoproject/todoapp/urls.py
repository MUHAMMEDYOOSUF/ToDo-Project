
from django.urls import path

from todoapp import views
app_name='todoapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    # path('',views.Tasklistview.as_view(),name='home'),
    # path('delete/<int:pk>/',views.Taskdeleteview.as_view(),name='delete'),
    # path('update/<int:pk>/',views.Taskupdateview.as_view(),name='update'),
]
