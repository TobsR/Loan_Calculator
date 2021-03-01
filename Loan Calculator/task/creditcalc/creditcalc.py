"""loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
print(f'{loan_principal}\n{first_month}\n{second_month}\n{third_month}\n{final_output}')
"""

'''        self.option = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal,
type "m" for the monthly payment:""")'''

'''from math import ceil, log
import argparse


def cast(number):
    for t in (int, float):
        try:
            n = t(number)
            return n
        except ValueError:
            pass


def check_positive(value):
    e_value = cast(value)
    if e_value < 0:
        print("Incorrect parameters")
    return e_value


def annuity_monthly_payments_number(principal, payment, interest):
    nominal_interest_rate = interest / 1200
    number_of_months = ceil(log(payment / (payment - (nominal_interest_rate * principal)),
                                1 + nominal_interest_rate))

    print(f"It will take {number_of_months // 12} years to repay this loan!" if number_of_months % 12 == 0 else
          f"It will take {number_of_months // 12} years and {number_of_months % 12} months to repay this loan!")
    print(f"Overpayment = {ceil((number_of_months * payment) - principal)}")


def annuity_monthly_payment_amount(principal, periods, interest):
    nominal_interest_rate = interest / 1200

    monthly_payment = principal * nominal_interest_rate * (1 + nominal_interest_rate) ** periods / \
                      ((1 + nominal_interest_rate) ** periods - 1)

    print(f"Your annuity payment = {ceil(monthly_payment)}!")
    print(f"Overpayment = {ceil((periods * ceil(monthly_payment)) - principal)}")


def annuity_loan_principal(payment, periods, interest):
    nominal_interest_rate = interest / 1200
    loan_principal = payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** periods) /
                                ((1 + nominal_interest_rate) ** periods - 1))
    print(f"Your loan principal = {round(loan_principal)}!")
    print(f"Overpayment = {ceil((periods * payment) - loan_principal)}")


def differentiated_payments(principal, periods, interest):
    nir = interest / 1200  # nominal interest rate
    dm = [ceil(principal / periods + nir * (principal - (principal * (m - 1)) / periods)) for m in range(1, periods + 1)]
    for month, payment in enumerate(dm, start=1):
        print(f"Month {month}: payment is {payment}")
    print(f"Overpayment = {sum(dm) - principal}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This module allows you to calculate all details about your loan")

    parser.add_argument(
        "--type",
        choices=["annuity", "diff"],
        help="Specify the type of payment"
    )
    parser.add_argument(
        "--payment",
        help="Indicate the monthly payment amount if the type of payment is 'annuity'",
        type=check_positive
    )
    parser.add_argument(
        "--principal",
        type=check_positive
    )
    parser.add_argument(
        "--periods",
        type=check_positive
    )
    parser.add_argument(
        "--interest",
        type=check_positive
    )

    args = parser.parse_args()

    if (args.type == "diff" and args.payment is not None) or args.interest is None or \
            list(vars(parser.parse_args()).values()).count(None) > 1:
        print("Incorrect parameters")
    elif args.type == "annuity":
        if args.principal is not None:
            if args.payment is not None:
                annuity_monthly_payments_number(args.principal, args.payment, args.interest)
            elif args.periods is not None:
                annuity_monthly_payment_amount(args.principal, args.periods, args.interest)
        else:
            annuity_loan_principal(args.payment, args.periods, args.interest)
    else:
        differentiated_payments(args.principal, args.periods, args.interest)
'''


import math
from sys import argv
import argparse

parser = argparse.ArgumentParser(description="loan calculator")
parser.add_argument("--type", choices=["annuity", "diff"], required=True)
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)  #, required=True

# arguments = ["--type", "--payment", "--principal", "--periods", "--interest"]


arguments = parser.parse_args()
if arguments.type == "diff" and arguments.payment != None:
    print("Incorrect parameters")
    exit()

if len(argv) < 4:
    print("Incorrect parameters")
    exit()

if arguments.payment != None and arguments.payment < 0:
    print("Incorrect parameters")
    exit()
if arguments.principal != None and arguments.principal < 0:
    print("Incorrect parameters")
    exit()
if arguments.periods != None and arguments.periods < 0:
    print("Incorrect parameters")
    exit()
if arguments.interest != None and arguments.interest < 0:
    print("Incorrect parameters")
    exit()

if arguments.interest == None:
    print("Incorrect parameters")
    exit()



class CreditCalc:

    def __init__(self):
        self.loan_principal = 0
        self.overpayment = 0
        self.loan_interest = 0
        self.i = 0.0  # nominal interest rate
        self.payment = 0
        self.payment_last = 0
        self.months = 0
        self.option = ''

    def ask_principal(self):
        # self.loan_principal = int(input("Enter the loan principal:"))
        pass

    def ask_option(self):
        if self.option == 'n':
            self.calc_months()
        elif self.option == 'a':
            self.calc_annuity()
        elif self.option == 'p':
            self.calc_principal()
        elif self.option == 'm':
            self.calc_amount()
        elif self.option == 'd':
            self.calc_differentiated()

    def calc_months(self):
        # self.ask_principal()
        # self.payment = int(input("Enter the monthly payment:"))
        # self.loan_interest = float(input("Enter the loan interest:"))
        self.calc_nominal_interest()
        self.months = math.ceil(math.log(self.payment / (self.payment - self.i * self.loan_principal), 1 + self.i))

        years = self.months // 12
        months = self.months % 12

        message = "It will take "
        if years == 1:
            message += f'{years} year'
        elif years > 1:
            message += f'{years} years'
        if months == 1:
            message += f'{months} month'
        elif months > 1:
            message += f'{months} months'

        message += ' to repay this loan!'

        print(message)

        self.overpayment = (self.payment * self.months) - self.loan_principal
        print(f'Overpayment = {self.overpayment}')

    def calc_annuity(self):
        # self.ask_principal()
        # self.months = int(input("Enter the number of periods:"))
        # self.loan_interest = float(input("Enter the loan interest:"))
        self.calc_nominal_interest()
        self.payment = math.ceil(self.loan_principal * (self.i * (1 + self.i) ** self.months) / ((1 + self.i) ** self.months - 1))
        print(f'Your annuity payment = {self.payment}!')

        self.overpayment = (self.payment * self.months) - self.loan_principal
        print(f'Overpayment = {self.overpayment}')

    def calc_principal(self):
        # annuity = float(input("Enter the annuity payment:"))
        annuity = self.payment
        # self.months = int(input("Enter the number of periods:"))
        # self.loan_interest = float(input("Enter the loan interest:"))
        self.calc_nominal_interest()
        self.loan_principal = annuity / ((self.i * math.pow(1 + self.i, self.months)) / (math.pow(1 + self.i, self.months) - 1))
        print(f'Your loan principal = {self.loan_principal}!')

        self.overpayment = (self.payment * self.months) - self.loan_principal
        print(f'Overpayment = {math.ceil(self.overpayment)}')

    def calc_amount(self):
        # self.months = int(input("Enter the number of months:"))
        if self.loan_principal / self.months % 1 == 0.0:
            self.payment = self.loan_principal / self.months
            print(f'\nYour monthly payment = {self.payment}')
        else:
            self.payment = math.ceil(self.loan_principal / self.months)
            self.payment_last = self.loan_principal - (self.months - 1) * self.payment
            print(f'\nYour monthly payment = {self.payment} and the last payment = {self.payment_last}.')

        self.overpayment = (self.payment * self.months + self.payment_last) - self.loan_principal
        print(f'Overpayment = {self.overpayment}')

    def calc_nominal_interest(self):
        self.i = (self.loan_interest / 100) / 12 * (100 / 100)

    def calc_differentiated(self):
        self.calc_nominal_interest()
        for i in range(self.months):
            self.payment = math.ceil(self.loan_principal / self.months + self.i * (self.loan_principal - (self.loan_principal * ((i+1) - 1)) / self.months))
            print(f'Month {i+1}: payment is {self.payment}')
            self.overpayment += self.payment

        self.overpayment -= self.loan_principal
        print(f'Overpayment = {self.overpayment}')

loan_calculator = CreditCalc()

if arguments.principal != None:
    loan_calculator.loan_principal = arguments.principal
else:
    loan_calculator.option = 'p'
if arguments.periods != None:
    loan_calculator.months = arguments.periods
else:
    loan_calculator.option = 'n'
if arguments.payment != None:
    loan_calculator.payment = arguments.payment
else:
    loan_calculator.option = 'a'

if arguments.type != "annuity":
    loan_calculator.option = 'd'

loan_calculator.loan_interest = arguments.interest

loan_calculator.ask_option()