from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at']
    search_fields = ['title', 'status']
    list_filter = ['status', 'created_at', 'updated_at']

@admin.register(TicketLog)
class TicketLogAdmin(admin.ModelAdmin):
    list_display = ['ticket']
    search_fields = ['ticket', 'action']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'user', 'created_at']
    search_fields = ['ticket', 'user']
    list_filter = ['created_at']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'created_at']
    search_fields = ['question', 'answer']
    list_filter = ['created_at']
