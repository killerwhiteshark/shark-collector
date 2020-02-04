##########################################################
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for cats index
  path('sharks/', views.sharks_index, name='index'),
  path('sharks/<int:shark_id>/', views.sharks_detail, name='detail'),
  path('sharks/create/', views.SharkCreate.as_view(), name='sharks_create'),
  path('sharks/<int:pk>/update/', views.SharkUpdate.as_view(), name='sharks_update'),
  path('sharks/<int:pk>/delete/', views.SharkDelete.as_view(), name='sharks_delete'),
]

##############################################################

###### FROM SHARK PROJECT URLS AND GOING TO MAIN_APP VIEWS