from loans.models import Loan

def add_loan(amount, interest_rate, ip_address, date_requested, bank, customer):
    loan = Loan(
        amount=amount,
        interest_rate=interest_rate,
        ip_address=ip_address,
        date_requested=date_requested,
        bank=bank,
        customer=customer,
    )
    loan.save()


def add_loans(loans):
    Loan.objects.bulk_create(loans)


def view_loans():
    loans = Loan.objects.all()
    for loan in loans:
        print(loan)


if __name__ == "__main__":
    # Adiciona um empréstimo
    add_loan(10000, 0.05, "192.168.0.1", "2023-08-02", "Banco do Brasil", "Fulano de Tal")

    # Adiciona vários empréstimos
    loans = [
        Loan(
            amount=10000,
            interest_rate=0.05,
            ip_address="192.168.0.1",
            date_requested="2023-08-02",
            bank="Banco do Brasil",
            customer="Fulano de Tal",
        ),
        Loan(
            amount=20000,
            interest_rate=0.06,
            ip_address="192.168.0.2",
            date_requested="2023-08-03",
            bank="Caixa Econômica Federal",
            customer="Beltrano de Souza",
        ),
    ]
    add_loans(loans)

    # Visualiza todos os empréstimos
    view_loans()
