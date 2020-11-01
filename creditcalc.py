import math
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=int, help="the credit principal")
parser.add_argument("--periods", type=int, help="monthly payment")
parser.add_argument("--interest", type=float, help="credit interst")
parser.add_argument("--type", type=str, help="annuity or diff")
parser.add_argument("--payment", type=float, help="monthly payment")
args = parser.parse_args()

operation = args.type

wynik = ''
if (len([x for x in args._get_kwargs() if x[1] is None])) > 1:
    print('Incorrect patameters')
    exit(0)

if operation == 'annuity':
    if args.principal is None:
        payment = args.payment
        count_of_month = args.periods
        credit_interest = args.interest
        i = 0 if credit_interest == 0 else credit_interest/(12*100)
        credit_principal = math.ceil(payment / ((i * math.pow((1 + i),
                                                          count_of_month))/(math.pow((1 + i), count_of_month) - 1)))
        wynik = f'Your credit principal = {credit_principal}!'
        print(wynik)
        overpayment = payment * count_of_month - credit_principal
        print(f'Overpayment = {overpayment}')

    if args.periods is None:
        credit_principal = args.principal
        monthly_payment = args.payment
        credit_interest = args.interest
        i = 0 if credit_interest == 0 else credit_interest/(12*100)
        amount_of_months = math.ceil(math.log((monthly_payment / (monthly_payment - (i * credit_principal))), 1 + i))
        wynik = f'You need '

        if amount_of_months / 12 > 1:
            wynik = wynik + str(amount_of_months // 12) + f' years '
        elif amount_of_months / 12 == 1:
            wynik = wynik + str(amount_of_months // 12) + f' year '

        if amount_of_months > 12 and amount_of_months % 12 != 0:
            wynik = wynik + 'and '

        if amount_of_months % 12 > 1:
            wynik = wynik + str(amount_of_months % 12) + ' months '
        elif math.ceil(amount_of_months) == 1 or math.ceil(amount_of_months % 12) == 1:
            wynik = wynik + '1 month '

        print(wynik, 'to repay this credit!')
        overpayment = monthly_payment * amount_of_months - credit_principal
        print(f'Overpayment = {overpayment}')

    if args.payment is None:
        credit_principal = args.principal
        count_of_month = args.periods
        credit_interest = args.interest
        i = 0 if credit_interest == 0 else credit_interest/(12*100)
        payment = math.ceil(credit_principal * (i * math.pow((1 + i), count_of_month) / (pow((1 + i), count_of_month) - 1)))
        wynik = f'Your annuity payment = {payment}!'
        print(wynik)
        overpayment = payment * count_of_month - credit_principal
        print(f'Overpayment = {overpayment}')

elif operation == "diff":
    if args.payment is None:
        total = 0
        credit_principal = args.principal
        periods = args.periods
        credit_interest = args.interest
        i = 0 if credit_interest == 0 else credit_interest/(12*100)
        for month in range(args.periods):
            diff_payment = math.ceil((credit_principal / periods) + (i * (credit_principal - ((credit_principal * month) / periods))))
            total += diff_payment
            print(f'Month {month + 1}: paid out {diff_payment}')
        print(f'Ovenpayment = {total - credit_principal}')
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")

if operation == 'n':
    credit_principal = int(input('Enter the credit principal: '))
    monthly_payment = int(input('Enter monthly payment: '))
    credit_interst = float(input('Enter credit interst: '))
    i = 0 if credit_interst == 0 else credit_interst/(12*100)
    amount_of_months = math.ceil(math.log((monthly_payment / (monthly_payment - (i * credit_principal))), 1 + i))
    #print(amount_of_months)
    wynik = f'You need '
    if amount_of_months / 12 > 1:
        wynik = wynik + str(amount_of_months // 12) + f' years '
    elif amount_of_months / 12 == 1:
        wynik = wynik + str(amount_of_months // 12) + f' year '
    if amount_of_months > 12 and amount_of_months % 12 != 0:
        wynik = wynik + 'and '
    if amount_of_months % 12 > 1:
        wynik = wynik + str(amount_of_months % 12) + ' months '
    elif math.ceil(amount_of_months) == 1 or math.ceil(amount_of_months % 12) == 1:
        wynik = wynik + '1 month '

    print(wynik, 'to repay this credit!')

if operation == 'p':
    payment = float(input('Enter monthly payment: '))
    count_of_month = int(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    i = 0 if credit_interest == 0 else credit_interest/(12*100)
    credit_principal = math.ceil(payment / ((i * math.pow((1 + i),
                                                          count_of_month))/(math.pow((1 + i), count_of_month) - 1)))
    wynik = f'Your credit principal = {credit_principal}!'
    print(wynik)
if operation == 'a':
    credit_principal = int(input('Enter the credit principal: '))
    count_of_month = int(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    i = 0 if credit_interest == 0 else credit_interest/(12*100)

    payment = math.ceil(credit_principal * (i * math.pow((1 + i), count_of_month) / (pow((1 + i), count_of_month) - 1)))
    wynik = f'Your annuity payment = {payment}!'
    print(wynik)


