from django.urls import path
from django.urls import path
from .views import ticket_list, ticket_detail, ticket_create
from .views import (
    TicketListCreateView, TicketDetailView,
    TicketLogListCreateView, TicketLogDetailView,
    CommentListCreateView, CommentDetailView,
    FAQListCreateView, FAQDetailView
)

urlpatterns = [
    path('tickets-create/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-details'),

    path('ticket-logs/', TicketLogListCreateView.as_view(), name='ticketlog-list-create'),
    path('ticket-logs/<int:pk>/', TicketLogDetailView.as_view(), name='ticketlog-detail'),

    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    path('faqs/', FAQListCreateView.as_view(), name='faq-list-create'),
    path('faqs/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
]

urlpatterns += [
    path('tickets/', ticket_list, name='ticket-list'),
    path('tickets/create/', ticket_create, name='ticket-create'),
    path('ticket/<int:pk>/', ticket_detail, name='ticket-detail'),
]