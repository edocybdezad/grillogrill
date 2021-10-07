from django.urls import include,path
from django.contrib.auth.views import LoginView
from . import views
from .views import ItemUpdate
 
urlpatterns = [
    path('',views.index, name='index'),
    path('manage/',views.manage, name='manage'),
    path("<int:pk>", ItemUpdate.as_view(), name="item-update"),
    path("login/", LoginView.as_view(template_name='homepage/login.html'), name="login"),    
    # path('import',views.menu_import, name='import'),
]
