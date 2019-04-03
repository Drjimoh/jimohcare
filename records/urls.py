from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('<int:patient_id>/record/', views.record, name='record'),

]