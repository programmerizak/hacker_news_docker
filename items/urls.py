from django.urls import path
from . import views


app_name = "items"

urlpatterns = [
	path('', views.home, name='home'),
    path('new', views.new, name='new'),
    path('past/', views.past, name='past'),
    path('comments/', views.comments, name='comments'),
    path('ask/', views.ask, name='ask'),
    path('show/', views.show, name='show'),
    path('jobs/', views.jobs, name='jobs'),
    ############## SEARCH FORM ###################
    path('search/', views.search_items, name='search_items'),
    ############## DETAIL PAGE #################
    path('detail/<uuid:item_id>/', views.item_detail, name='item_detail'),
    ############## LOGIN USERS ###################
    path('submit/', views.submit, name='submit'),
    path('threads/', views.threads, name='threads'),

]
