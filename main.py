def annualizedReturn(profits):
  '''
  profits: tuple of floats
  '''
  
  finalReturn = 1
  n = len(profits)
  
  for i in range(n - 1):
    finalReturn *= (1 + profits[i])
  
  finalReturn *= (1 + profits[n - 1]) ** (1 / n)
  
  return finalReturn - 1
  

class Portfolio:
  
  def __init__(self, stocks):
    '''
    stocks: array of class Stock
    '''
    
    self.stocks = stocks
  
  def profit(self, initialDate, finalDate):
    '''
    initialDate: date
    finalDate: date
    '''
    
    stockProfits = (stock.price(finalDate) - stock.price(initialDate) / stock.price(initialDate) for stock in self.stocks)
    
    return annualizedReturn(stockProfits)