def lowestPayment (balance, annualInterestRate):
    """
    lowestPayment function calculates minimum monthly payment, which is multiply
    of 10 enough to pay all debt in 12 months
    balance - initial debt, int or float
    annualInterestRate - float i.e. 0.12
    mpr - monthly payment rate
    """
    tBal = balance
    air = annualInterestRate
    mpr = 10

    while balanceCalc (tBal, air, mpr) > 0:
        mpr += 10
    return mpr


def balanceCalc(tBal, air, mpr):
    """
    calculating balance with testing montly payment
    returning balance after 12 months
    """
    i = 1
    while i <= 12:
        tBal = ((tBal - mpr) + (tBal - mpr)*air/12)
        i += 1
    return tBal

print ("Lowest Payment:", lowestPayment(3379, 0.2))
