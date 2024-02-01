from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status

from loans.models import Loan, Payment
from loans.serializers import LoanSerializer, PaymentSerializer


class LoanViewSet(ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [
        DjangoModelPermissionsOrAnonReadOnly,
    ]


class LoanDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [
        DjangoModelPermissionsOrAnonReadOnly,
    ]

# ... outros endpoints ...

class LoanCreateView(CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def post(self, request: request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def post(self, request: request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_balance(request: request, loan_id: int):
    loan = Loan.objects.get(id=loan_id)
    serializer = LoanSerializer(loan)
    return Response(serializer.data)