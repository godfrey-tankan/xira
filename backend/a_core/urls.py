"""
URL configuration for a_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from a_home.views import *
from a_users.views import *
from a_bot.webhooks import webhook
from a_bot.accept_ticket import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name='profile'),
    path('webhook/', webhook, name='webhook'),
]
urlpatterns += [
    path('tickets/edit/<int:pk>/', TicketEditView.as_view(), name='ticket-edit'),
    path('tickets-create/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-details'),

    path('ticket-logs/', TicketLogListCreateView.as_view(), name='ticketlog-list-create'),
    path('ticket-logs/<int:pk>/', TicketLogDetailView.as_view(), name='ticketlog-detail'),
    path('tickets/delete/<int:pk>/', TicketDeleteView.as_view(), name='ticket-delete'),

    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    path('faqs/', FAQListCreateView.as_view(), name='faq-list-create'),
    path('faqs/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
    path('tickets/', ticket_list, name='ticket-list'),
    path('tickets/create/', ticket_create, name='ticket-create'),
    path('ticket/<int:pk>/', ticket_detail, name='ticket-detail'),
    path('handle-enquiry/', handle_inquiry, name='handle-enquiry'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)