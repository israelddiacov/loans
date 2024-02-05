from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status, routers, serializers, viewsets
from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema

from loans.models import Loan, Payment
from loans.serializers import LoanSerializer, PaymentSerializer


class LoanViewSet(ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    filter_fields = ['date_requested', 'amount', 'bank']
    ordering_fields = ['date_requested', 'amount']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class LoanDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class LoanCreateView(CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@api_view(["GET"])
def get_balance(request, pk):
    try:
        loan = Loan.objects.get(id=pk)
    except Loan.DoesNotExist:
        return Response({"error": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)

    # Calculando o saldo
    payments = loan.payments.all()
    total_paid = sum(payment.amount for payment in payments)

    balance = loan.amount - total_paid

    return Response({"balance": balance})
