from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('krnotes/', include('krnotes.urls')),
    path('krnotes/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('krnotes/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('todo/', include('todo.urls')),
    path('dndcc/', include('dndcc.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
