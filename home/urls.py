
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.dash,name='dash'),
    path('',views.dashboard, name='dashboard'),
    path('home',views.dashboard, name='dashboard'),

    path('session', views.session, name='session'),
    path('add-ac', views.add_activity, name="Add Activity")
]
