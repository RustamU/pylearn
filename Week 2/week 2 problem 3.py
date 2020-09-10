def lowestPayment (balance, annualInterestRate):
    """
    lowestPayment function calculates minimum monthly payment, which is multiply
    of 10 enough to pay all debt in 12 months
    balance - initial debt, int or float
    annualInterestRate - float i.e. 0.12
    mpr - monthly payment rate, float or int
    lower - initial lower bound, float
    upper - initial upper bound, float
    """
    tBal = balance
    air = annualInterestRate
    lower = balance / 12
    upper = (balance * (1 + air)**12)/12
    mpr = (lower + upper)/2

#comparing final balance with zero.
#final balance calculating in balanceCalc function
#if result is positive - choosing new mpr between current mpr and upper limit
#if result is negative - choosing new mpr between current mpr and lower limit
    while round (balanceCalc (tBal, air, mpr), 2) != 0:
        mpr = (lower + upper)/2
        if round (balanceCalc (tBal, air, mpr), 2) > 0:
            lower = mpr
        if round (balanceCalc (tBal, air, mpr), 2) < 0:
            upper = mpr
    return (round(mpr,2))


def balanceCalc(tBal, air, mpr):
    """
    calculating balance with testing montly payment
    returning balance after 12 months just to take some code away from
    lowestPayment function
    """
    i = 1
    while i <= 12:
        tBal = ((tBal - mpr) + (tBal - mpr)*air/12)
        i += 1
    return tBal

print ("Lowest Payment:", lowestPayment(320000, 0.2))
