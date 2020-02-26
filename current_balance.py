def current_balance(credits, debits):
    """
    Check balance function that returns the current balance
    taking into consideration all the debits and credits
    of the last 24 hours
    """
    start_balance = 0 # zero here is only a placeholder
    new_balance = (start_balance + credits()) - debits()
    return new_balance