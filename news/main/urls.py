from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.newproject, name='project'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('test/', views.test, name='test'),
    path('user/', views.userPage, name='user-page'),
    path('manager/', views.managerPage, name='manager-page'),
    path('register/', views.registerPage, name='register'),
    path('women/', views.women),
    path('men/', views.men),
    path('news_home/', views.news_home, name='add-post'),
    path('sportnews/', views.form, name='sportnews'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:id>/delete', views.delete, name='news-delete'),
    path('forupload/', views.forupload, name='video-upload'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)