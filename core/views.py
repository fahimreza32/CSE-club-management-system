from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Member, MembershipPayment, Event, Expenditure
from .forms import MemberForm, MembershipPaymentForm, EventForm, ExpenditureForm
import json
from datetime import datetime
from django.shortcuts import render
from django.db.models import Sum
import json
from .models import Member, MembershipPayment, Event, Expenditure

def dashboard(request):
    # Counts and sums
    total_members = Member.objects.count()
    membership_income = MembershipPayment.objects.aggregate(total=Sum('amount'))['total'] or 0
    event_income = Event.objects.aggregate(total=Sum('income'))['total'] or 0
    expense = Expenditure.objects.aggregate(total=Sum('amount'))['total'] or 0
    final_income = membership_income + event_income - expense
    # Convert Decimals to float for JSON
    chart_labels = ['Membership', 'Event', 'Expenses']
    chart_data = [float(membership_income), float(event_income), float(expense)]
    context = {
        'total_members': total_members,
        'membership_income': membership_income,
        'event_income': event_income,
        'expense': expense,
        'final_income': final_income,
        'chart_labels_json': json.dumps(chart_labels),
        'chart_data_json': json.dumps(chart_data),
        'current_year': datetime.now().year,
    }
    return render(request, 'core/dashboard_main.html', context)
# Member CRUD
def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_dashboard')
    else:
        form = MemberForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Member'})

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect('member_dashboard')
    return render(request, 'core/form.html', {'form': form, 'title': 'Edit Member'})

def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('member_dashboard')

# Membership Payment CRUD
def add_payment(request):
    
    if request.method == "POST":
        form = MembershipPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_dashboard')
    else:
        form = MembershipPaymentForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Membership Payment'})

# Event CRUD
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_dashboard')
    else:
        form = EventForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Event'})

# Expenditure CRUD
def add_expenditure(request):
    if request.method == "POST":
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_dashboard')
    else:
        form = ExpenditureForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Expenditure'})

# Separate Segment Dashboards
def member_dashboard(request):
    members = Member.objects.all()
    return render(request, 'core/dashboard_members.html', {'members': members})

def payment_dashboard(request):
    payments = MembershipPayment.objects.all()
    payments = MembershipPayment.objects.select_related('member').all()
    final_income = payments.aggregate(total=Sum('amount'))['total'] or 0
    context = {
        'payments': payments,
        'final_income': final_income,
    }
    return render(request, 'core/dashboard_payments.html', context)  

def event_dashboard(request):
    events = Event.objects.all()
    events = Event.objects.all()
    total_income = events.aggregate(total=Sum('income'))['total'] or 0
    context = {
        'events': events,
        'total': total_income,  # matches your template variable {{ total }}
    }
    return render(request, 'core/dashboard_events.html', context)
    
def expense_dashboard(request):
    expenses = Expenditure.objects.all()
    total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
    context = {
        'expenses': expenses,
        'total': total_expense,  # matches {{ total }} in template
    }
    return render(request, 'core/dashboard_expenses.html', context)