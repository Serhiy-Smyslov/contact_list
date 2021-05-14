from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact/', views.add_contact, name='add_contact'),
    path('profile/<str:pk>', views.contact_profile, name='contact_profile'),
    path('edit-contact/<str:pk>', views.edit_contact, name='edit_contact'),
    path('delete/<str:pk>', views.delete_contact, name='delete_contact'),
]
