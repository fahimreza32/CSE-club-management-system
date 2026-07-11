from django.contrib import admin
from .models import Member, MembershipPayment, Event, Expenditure
admin.site.register(Member)
admin.site.register(MembershipPayment)
admin.site.register(Event)
admin.site.register(Expenditure)
