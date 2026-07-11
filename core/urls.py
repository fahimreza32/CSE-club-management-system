from django.urls import path
from . import views
urlpatterns = [
    # Home page/dashboard
    path('', views.dashboard, name='main_dashboard'),  # <-- Use 'dashboard' view
    # Member URLs
    path('members/', views.member_dashboard, name='member_dashboard'),
    path('members/add/', views.add_member, name='add_member'),
    path('members/edit/<int:pk>/', views.edit_member, name='edit_member'),
    path('members/delete/<int:pk>/', views.delete_member, name='delete_member'),
    # Membership Payment URLs
    path('payments/', views.payment_dashboard, name='payment_dashboard'),
    path('payments/add/', views.add_payment, name='add_payment'),
    # Event URLs
    path('events/', views.event_dashboard, name='event_dashboard'),
    path('events/add/', views.add_event, name='add_event'),
    # Expenditure URLs
    path('expenses/', views.expense_dashboard, name='expense_dashboard'),
    path('expenses/add/', views.add_expenditure, name='add_expenditure'),
]