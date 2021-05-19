from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView,PostUpdateView,PostDeleteView,PostListView2,PostListView3
urlpatterns = [
  path('', PostListView.as_view(), name='Estate-home'),
  path('house/', PostListView2.as_view(), name='Estate-house'),
  path('apartments/', views.apartments, name='Estate-apartments'),
  path('register/', views.register, name='Estate-register'),
  path('login/', views.log_in, name='Estate-log in'),
  path('profile/', PostListView3.as_view(), name='Estate-profile'),
  path('page/', views.home2, name='Estate-home2'),
  path('logout/', views.log_out, name='Estate-logout'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='Estate-detail'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='Estate-update'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='Estate-delete'),
  path('post/new/', PostCreateView.as_view(), name='Estate-create')



]
