from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from loans.models import Loan, Payment
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class LoanPaymentCreationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_create_loan(self):
        url = reverse('loan-create')
        data = {
            'amount': 1000.0,
            'interest_rate': 0.05,
            'ip_address': '192.168.1.1',
            'date_requested': '2024-02-01',
            'bank': 'Meu Banco',
            'customer': 'Cliente 1',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 1)

    def test_create_payment(self):
        loan = Loan.objects.create(
            amount=1000.0,
            interest_rate=0.05,
            ip_address='192.168.1.1',
            date_requested='2024-02-01',
            bank='Meu Banco',
            customer='Cliente 1',
        )
        url = reverse('payment-create')
        data = {
            'loan': loan.id,
            'date': '2024-02-15',
            'amount': 200.0,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

class LoanViewTests(APITestCase):
    def test_view_loans(self):
        url = reverse('loan-list')  # Use a URL correta para a listagem de empréstimos
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Verifica se há dados retornados


class PaymentViewTests(APITestCase):
    def test_view_payments(self):
        url = reverse('payment-create')  # Ajuste conforme suas URLs
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Verifica se há dados retornados

class BalanceCalculationTests(APITestCase):
    def test_balance_calculation(self):
        loan = Loan.objects.create(
            amount=1000.0,
            interest_rate=0.05,
            ip_address='192.168.1.1',
            date_requested='2024-02-01',
            bank='Meu Banco',
            customer='Cliente 1',
        )
        url = reverse('loan-balance', args=[loan.id])  # Ajuste conforme suas URLs
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('balance', response.data)  # Verifica se 'balance' está presente na resposta
