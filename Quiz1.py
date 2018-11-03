#Quiz 1 Instructions:
#Kathryn bought 600 shares of stocks at a price of 21.77 per share.
#she must pay her stock broker a 2% commission for the transaction
# do the following: the amount paid for the stock alone(without commission)
#the amount of commission
#the total amount paid(stock plus commission)
#display each and dont forget to comment



#setting the values 
shares = 600
stock_price = 21.77
comm = .02

#calculations
amount_stock = shares * stock_price
amount_comm = comm * amount_stock
amount_total = amount_stock + amount_comm




#print statements
print('the price she paid for just the stock is: ',amount_stock, 'dollars')
print('the amount of commission her broker will recieve is: ',amount_comm, 'dollars')
print('the amount Kathryn will pay in total is:',amount_total,'dollars')
