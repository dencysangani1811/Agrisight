from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.homedesign,name='homedesign'),
    path('login',views.loginPage,name='login'),
    path('register',views.register,name='register'),
    path('page',views.page,name='page'),
     path('logout',views.logoutUser,name='logout'),
     path('detect',views.detect,name='detect'),
     path('dis_detect',views.dis_detect,name='dis_detect')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
