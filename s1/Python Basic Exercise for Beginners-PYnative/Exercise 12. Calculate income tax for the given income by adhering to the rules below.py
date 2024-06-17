# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

def tax_count(income):

    if income < 10000:
        rate = 0  # (0%)

        payable = rate * income / 100

        return payable

    elif 20000 > income > 10000:
        income -= 10000
        rate = 10  # (10%)

        payable = rate * income / 100

        return payable
    else:
        # for 10,000 tax: 10%
        rate = 10
        payable = 10000 * rate / 100

        # remaining tax: 20%
        rate = 20
        payable += (income - 20000) * rate / 100

        return payable


print("Total tax:", tax_count(50000))
