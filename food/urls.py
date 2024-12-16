from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('items/',views.items,name='items'),
    #add item
    #path('add',views.create_item,name='create_item'),
    path('add',views.CreateItem.as_view(),name='create_item'),
    path('update/', views.update, name='update', kwargs={'id': None}),
    path('update/<int:item_id>/',views.update,name='update'),
    path('delete/<int:item_id>/',views.delete,name='delete'),
]
