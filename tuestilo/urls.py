from django.urls import path
from  . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(''                , views.base,                      name = 'base'      ),
    path('info'            , views.info,                      name = 'info'      ),
    path('catalogo'        , views.catalogo,                  name = 'catalogo'  ),
    path('contacto'        , views.contacto,                  name = 'contacto'  ),
    path('carro'           , views.carro,                     name = 'carro'     ),
    path('register'        , views.register,                  name = 'register'  ),
    path('crud'            , views.crud,                      name= 'crud'       ),
    path('crud/add'        , views.add_user,                  name= 'add_user'   ),
    path('crud/edit/<int:user_id>/'   , views.edit_user,      name= 'edit_user'  ),
    path('crud/delete/<int:user_id>/' , views.delete_user,    name= 'delete_user'),
    path('accounts/login/' , views.CustomLoginView.as_view(), name= 'login      '),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name= 'logout'     ),
]