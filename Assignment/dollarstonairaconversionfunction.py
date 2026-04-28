def dollars_to_naira(amount_in_dollars):
    dollar_rate = 1550
    naira_amount = amount_in_dollars * dollar_rate
    
    return round(naira_amount, 2)
