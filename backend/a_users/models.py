from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True) 
    
    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayname:
            return self.displayname
        return self.user.username 
    
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return static("images/avatar.svg")


class TicketStatus(models.TextChoices):
    OPEN = 'OPEN'
    PENDING = 'PENDING'
    CLOSED = 'CLOSED'
    CANCELLED = 'CANCELLED'
    EXPIRED = 'EXPIRED'

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requester = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tickets_requested',null=True, blank=True)
    assigned_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tickets_assigned', null=True, blank=True)
    status = models.CharField(max_length=20, choices=TicketStatus.choices, default=TicketStatus.OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status}"

class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    commented_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.commented_by.name} - {self.ticket.title}"