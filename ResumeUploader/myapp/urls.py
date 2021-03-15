
from django import views
from django.contrib import admin
from django.urls import path
from myapp import views # type: ignore


from django import views
from django.contrib import admin
from django.urls import path
from myapp import views # type: ignore


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('loggedout/', views.UserLogoutView.as_view(), name='loggedout'),
    path('profile/', views.Dashboard.as_view(), name='dashboard'),
    path('view/<int:pk>', views.CandidateView.as_view(), name='candidate'),
    path('edit/<int:pk>', views.CandidateUpdate.as_view(), name='editcandidate'),
]


