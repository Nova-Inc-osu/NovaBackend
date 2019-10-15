from django.contrib import admin
from nova.models import Doctor, Patient, Conversation, Message

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Conversation)
admin.site.register(Message)