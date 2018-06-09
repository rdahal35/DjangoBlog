from django.urls import path
from blog import views




urlpatterns = [
    
   path('', views.post_list, name='post_list'),
   path('newpost/', views.add_post, name='post_new'),
   path('<int:post_id>/editpost/', views.edit_post, name='edit_post'),
   path('<int:post_id>/', views.post_detail, name='post_detail'),
   path('signup/',views.signup, name='signup' ),
]