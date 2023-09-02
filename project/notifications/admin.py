from django.contrib import admin
from .models import Notification
from django import forms

# Register your models here.

class SendNotificationForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Notification Message", max_length=500)
    # recipient = forms.CharField()

    # def send_notification(self):
    #     message = self.cleaned_data['message']
    #     recipient = self.cleaned_data['recipient']
    #     Notification.objects.create(message=message, recipient=recipient)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    add_form_template = 'admin/custom_add_form.html'