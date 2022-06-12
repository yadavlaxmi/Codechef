withdrawal_amount, balance_amount = input().split()              
withdrawal_amount = int(withdrawal_amount)                        
balance_amount = float(balance_amount)                            
if (withdrawal_amount % 5 == 0 and balance_amount>=(withdrawal_amount+0.5)):
    balance_amount = balance_amount - withdrawal_amount - 0.5     
    print(round(balance_amount,2))
else:
    print(round(balance_amount,2))

    # atm