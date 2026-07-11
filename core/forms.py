from django import forms
from .models import Member, MembershipPayment, Event, Expenditure
COMMON_INPUT_CLASS = "w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': COMMON_INPUT_CLASS}),
            'email': forms.EmailInput(attrs={'class': COMMON_INPUT_CLASS}),
            'phone': forms.TextInput(attrs={'class': COMMON_INPUT_CLASS}),
        }

class MembershipPaymentForm(forms.ModelForm):
    class Meta:
        model = MembershipPayment
        fields = ['member', 'amount']
        widgets = {
            'member': forms.Select(attrs={'class': COMMON_INPUT_CLASS}),
            'amount': forms.NumberInput(attrs={'class': COMMON_INPUT_CLASS}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_date', 'income']
        widgets = {
            'name': forms.TextInput(attrs={'class': COMMON_INPUT_CLASS}),
            'event_date': forms.DateInput(
                attrs={'type': 'date', 'class': COMMON_INPUT_CLASS}
            ),
            'income': forms.NumberInput(attrs={'class': COMMON_INPUT_CLASS}),
        }

class ExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ['description', 'amount']
        widgets = {
            'description': forms.TextInput(attrs={'class': COMMON_INPUT_CLASS}),
            'amount': forms.NumberInput(attrs={'class': COMMON_INPUT_CLASS}),
        }
