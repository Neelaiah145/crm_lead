from django.contrib import admin
from django.urls import path
from leads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view(), name='login'),
    path('leads/',views.ContactList.as_view(),name="contact_lead"),
    path("lead/edit/<int:pk>/",views.EditLeadContact.as_view(),name="edit_lead"),
    path("delete_lead/<int:id>/", views.DeleteLeadManagement.as_view(), name="delete_lead"),
    path("delete_lead/", views.DeleteLeadManagement.as_view(), name="delete_leads"),
    
]