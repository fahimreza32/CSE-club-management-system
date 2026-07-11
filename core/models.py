from django.db import models
# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class MembershipPayment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.member.name} - {self.amount}"

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Expenditure(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.description