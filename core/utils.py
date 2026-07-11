from django.db.models import Sum
from .models import MembershipPayment, Event, Expenditure

def get_final_income():
    total_membership = MembershipPayment.objects.aggregate(total=Sum('amount'))['total'] or 0
    total_event_income = Event.objects.aggregate(total=Sum('income'))['total'] or 0
    total_expenditure = Expenditure.objects.aggregate(total=Sum('amount'))['total'] or 0
    final_income = total_membership + total_event_income - total_expenditure
    return final_income