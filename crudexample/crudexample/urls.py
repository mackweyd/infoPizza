from django.contrib import admin  
from django.urls import path  
from employee import views  
urlpatterns = [  
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('cardapio/index.html',views.cardapioIndex),
    path('cardapio/edit/<int:id>',views.cardapioEdit),
    path('cardapio/update/<int:id>',views.cardapioUpdate),
    path('cardapio/delete/<int:id>',views.cardapioDestroy),
    #path('pedidos/index.html'),
    #path('cozinha/index.html'),
    path('insert',views.insert),
    path('emp', views.emp),  
    path('employee/show',views.show),  
    path('employee/edit/<int:id>', views.edit),  
    path('employee/update/<int:id>', views.update),  
    path('employee/delete/<int:id>', views.destroy),  
]  