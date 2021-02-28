"""loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
print(f'{loan_principal}\n{first_month}\n{second_month}\n{third_month}\n{final_output}')
"""
import math


class CreditCalc:

    def __init__(self):
        self.loan_principal = 0
        self.payment = 0
        self.payment_last = 0
        self.months = 0
        self.option = ''

    def ask_principal(self):
        self.loan_principal = int(input("Enter the loan principal:"))

    def ask_option(self):
        self.option = input("""What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:""")
        if self.option == 'm':
            self.calc_months()
        elif self.option == 'p':
            self.calc_amount()

    def calc_months(self):
        self.payment = int(input("Enter the monthly payment:"))
        self.months = math.ceil(self.loan_principal / self.payment)
        if self.months == 1:
            add_this = ""
        else:
            add_this = "s"
        print(f'\nIt will take {self.months} month{add_this} to repay the loan')

    def calc_amount(self):
        self.months = int(input("Enter the number of months:"))
        if self.loan_principal / self.months % 1 == 0.0:
            self.payment = self.loan_principal / self.months
            print(f'\nYour monthly payment = {self.payment}')
        else:
            self.payment = math.ceil(self.loan_principal / self.months)
            self.payment_last = self.loan_principal - (self.months - 1) * self.payment
            print(f'\nYour monthly payment = {self.payment} and the last payment = {self.payment_last}.')


loan_calculator = CreditCalc()
loan_calculator.ask_principal()
loan_calculator.ask_option()
