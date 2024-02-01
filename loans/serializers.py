from rest_framework import serializers
from loans.models import Loan, Payment


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "id",
            "amount",
            "interest_rate",
            "ip_address",
            "date_requested",
            "bank",
            "customer",
            "balance",
        ]

    def get_balance(self, loan: Loan):
        # Calcula o saldo devedor usando juros compostos pro rata dia
        payments = loan.payments.all()
        total_payments = sum(payment.amount for payment in payments)
        interest_rate = loan.interest_rate / 365
        balance = loan.amount * (1 + interest_rate) ** (payments.count() - 1) - total_payments
        return balance


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["loan", "date", "amount"]
