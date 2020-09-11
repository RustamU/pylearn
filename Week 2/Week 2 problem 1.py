def balanceCalc(balance, annualInterestRate, monthlyPaymentRate):
    """
    function prints year credit balance based on minimum monthly monthly payment
    rounded to two decimal digits
    balance - initial balance, float or int
    annualInterestRate - annual interest, float
    monthlyPaymentRate - minimum possible part of debt paid monthly, float
    tBal - variable for store current balance, float
    """
    tBal = balance
    i = 1
    while i <= 12:
        tBal = ((tBal - tBal*monthlyPaymentRate) + (tBal - tBal*monthlyPaymentRate)*annualInterestRate/12)
        i += 1
    return round (tBal, 2)

print ('Remaining balance:', balanceCalc (balance, annualInterestRate, monthlyPaymentRate))
