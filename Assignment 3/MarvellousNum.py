def ChkPrime(no):
    if (no == 1):
        return False
    elif (no == 2):
        return True
    else:
        for i in range(2,no):
            if no % i == 0:
                return False
        return True