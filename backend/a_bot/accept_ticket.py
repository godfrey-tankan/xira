import contextlib
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from a_home.models import *
from django.contrib.auth.models import Group

def handle_inquiry(wa_id, response, name):
    ticket = Ticket(
        title=f"Inquiry from {name}",
        description=response,
        created_by=wa_id[0], 
        status='open'
    )
    ticket.save()
    # Log the ticket creation
    TicketLog.objects.create(
        ticket=ticket,
        status='open',
        changed_by=wa_id[0]
    )
    # Broadcast to support members
    with contextlib.suppress(Group.DoesNotExist):
        support_group = Group.objects.get(name='Support')
        support_members = User.objects.filter(groups=support_group)
        for support_member in support_members:
            ...
        
    response = 'Thank you for contacting us. A support member will be with you shortly.'

    return response

@csrf_exempt
def accept_ticket(wa_id,name, ticket_id):
    support_member = wa_id[0]
    try:
        ticket = Ticket.objects.get(id=ticket_id, status='open')
        ticket.assigned_to = support_member
        ticket.status = 'pending'
        ticket.save()
        
        # Log the status change
        TicketLog.objects.create(
            ticket=ticket,
            status='pending',
            changed_by=support_member
        )
        
        return f"Ticket #{ticket.id} assigned to {name}"
    except Ticket.DoesNotExist:
        return "Ticket not available or already assigned"
