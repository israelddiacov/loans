from django.db import models

class Loan(models.Model):
    app_label = 'loans'  # Adicione esta linha
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    ip_address = models.GenericIPAddressField()
    date_requested = models.DateField()
    bank = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)

    class Meta:
        ordering = ["-date_requested"]


class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
