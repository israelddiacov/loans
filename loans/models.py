from django.db import models

class Loan(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    ip_address = models.GenericIPAddressField()
    date_requested = models.DateField()
    bank = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["-date_requested"]

class Payment(models.Model):
    loan = models.ForeignKey(Loan, related_name='payments', on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)