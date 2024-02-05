from rest_framework import serializers
from loans.models import Loan, Payment
from datetime import datetime

class LoanSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    payments = serializers.SerializerMethodField()

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
            "payments",
        ]

    def get_balance(self, loan: Loan):
        payments = loan.payments.all()
        total_payments = sum(payment.amount for payment in payments)
        interest_rate = loan.interest_rate / 365
        days_since_loan = (datetime.now().date() - loan.date_requested).days
        balance = loan.amount * (1 + interest_rate) ** days_since_loan - total_payments
        return balance
from rest_framework import serializers
from loans.models import Loan, Payment
from datetime import datetime

class LoanSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    payments = serializers.SerializerMethodField()

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
            "payments",
        ]


    def get_balance(self, loan: Loan):
        payments = loan.payments.all()
        total_payments = sum(payment.amount for payment in payments)
        interest_rate = loan.interest_rate / 365
        days_since_loan = (datetime.now().date() - loan.date_requested).days
        balance = loan.amount * (1 + interest_rate) ** days_since_loan - total_payments
        return balance

    def get_payments(self, loan: Loan):
        # Método para obter os pagamentos relacionados a um empréstimo
        payments = loan.payments.all()
        payment_data = [{"date": payment.date, "amount": payment.amount} for payment in payments]
        return payment_data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["loan", "date", "amount"]
