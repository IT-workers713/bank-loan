from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('loan/', views.loan,name='loan'),
    path('loan_prediction/', views.loan_predict,name='loanpred'),

]