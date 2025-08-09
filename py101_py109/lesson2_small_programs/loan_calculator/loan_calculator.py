print('Welcome to Loan Calculator!')

while True:
    loan_amount = float(input('Enter loan amount: '))
    loan_duration_years = float(input('Enter loan duration in years: '))
    apr = float(input('Enter Annual Percentage Rate (APR): e.g 5 for 5%, 10.5 for 10.5% ')) / 100

    montly_interest_rate = apr / 12
    loan_duration_months = loan_duration_years * 12

    monthly_payment = loan_amount * (montly_interest_rate / (1 - (1 + montly_interest_rate) ** (-loan_duration_months)))

    total_payment = monthly_payment * loan_duration_months
    print(total_payment)

    total_interest = total_payment - loan_amount
    print(total_interest)

    print(f'Payment Every Month: ${monthly_payment:.2f}')
    print(f'Total of {loan_duration_months} Payments: ${total_payment:.2f}')
    print(f'Total Interest: ${total_interest:.2f}')

    ans = input('Calculate another loan? y/n ').lower()

    while True:
        if ans.startswith('y') or ans.startswith('n'):
            break

        print('Please enter "y" or "n".')
        ans = input().lower()

    if ans[0] == 'n':
        break

