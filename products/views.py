from django.http import  HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Loan

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})


def message(request):
    return HttpResponse("new product")



@app.route('/loan', methods=['POST'])
def add_loan():
  name = request.json['name']
  annualInterestRate = request.json['annualInterestRate']
  numberOfYears = request.json['numberOfYears']
  loanAmount = request.json['loanAmount']
  monthlyPayment = request.json['monthlyPayment']


  new_loan = Loan(name, annualInterestRate, numberOfYears, loanAmount, monthlyPayment)

  db.session.add(new_loan)
  db.session.commit()

  return loan_schema.jsonify(new_loan)

# Get All loans
@app.route('/loan', methods=['GET'])
def get_loans():
  all_loans = Loan.query.all()
  result = loans_schema.dump(all_loans)
  return jsonify(result.data)

# Get Single loans
@app.route('/loan/<id>', methods=['GET'])
def get_loan(id):
  loan = Loan.query.get(id)
  return loan_schema.jsonify(loan)

# Update a loan
@app.route('/loan/<id>', methods=['PUT'])
def update_loan(id):
  loan = Loan.query.get(id)

  name = request.json['name']
  annualInterestRate = request.json['annualInterestRate']
  numberOfYears = request.json['numberOfYears']
  loanAmount = request.json['loanAmount']
  monthlyPayment = request.json['monthlyPayment']

  loan.name = name
  loan.annualInterestRate = annualInterestRate
  loan.numberOfYears = numberOfYears
  loan.loanAmount = loanAmount
  loan.monthlyPayment = monthlyPayment

  db.session.commit()

  return loan_schema.jsonify(loan)

# Delete loan
@app.route('/loan/<id>', methods=['DELETE'])
def delete_loan(id):
  loan = Loan.query.get(id)
  db.session.delete(loan)
  db.session.commit()

  return loan_schema.jsonify(loan)


  # compute the total payment. 2
def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    # compute the monthly payment.1
def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / \
            (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment



