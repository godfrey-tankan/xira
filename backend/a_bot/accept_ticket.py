from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from a_home.models import *
from django.contrib.auth.models import Group

def handle_inquiry(wa_id, response, name):
    ticket = Ticket.objects.create(
        title=f"Inquiry from {name}",
        description=response,
        created_by=wa_id[0], 
        status='open'
    )
    # Log the ticket creation
    TicketLog.objects.create(
        ticket=ticket,
        status='open',
        changed_by=wa_id[0]
    )
    # Broadcast to support members
    support_group = Group.objects.get(name='Support')
    support_members = User.objects.filter(groups=support_group)
    
    for member in support_members:
        pass
    
    return JsonResponse({"status": "Ticket created", "ticket_id": ticket.id})

@csrf_exempt
def accept_ticket(request, ticket_id):
    support_member = request.user  
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
        
        return JsonResponse({"status": "Ticket assigned", "ticket_id": ticket.id})
    except Ticket.DoesNotExist:
        return JsonResponse({"status": "Ticket not available or already assigned"}, status=400)
