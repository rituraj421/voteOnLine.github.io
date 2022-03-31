# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from authentication import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeView, name='home'),
    path('register/', views.registrationView, name='registration'),
    path('login/', views.loginView, name='login'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('logout/', views.logoutView, name='logout'),
    path('position/', views.positionView, name='position'),
    path('candidate/<int:pos>/', views.candidateView, name='candidate'),
    path('candidate/detail/<int:id>/', views.candidateDetailView, name='detail'),
    path('result/', views.resultView, name='result'),
    path('changepass/', views.changePasswordView, name='changepass'),
    path('editprofile/', views.editProfileView, name='editprofile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Online Voting System"
admin.site.index_title = "Welcome to RAIT-SUC online voting system"
admin.site.site_title = "RAIT-SUC voting site"