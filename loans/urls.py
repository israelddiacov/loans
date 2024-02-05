"""
URL configuration for loans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from loans.views import LoanCreateView, PaymentCreateView, LoanViewSet, LoanDetailsView, get_balance
from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/loans/", LoanCreateView.as_view(), name="loan-create"),
    path("api/loans/payments/", PaymentCreateView.as_view(), name="payment-create"),
    path("api/loans/<int:pk>/", LoanDetailsView.as_view(), name="loan-detail"),
    path("api/loans/<int:pk>/balance/", get_balance, name="loan-balance"),
    path("api/loans/", LoanViewSet.as_view(), name="loan-list"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
