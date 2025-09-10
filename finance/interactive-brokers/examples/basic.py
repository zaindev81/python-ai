from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Paper: 7497 Production: 7496

contract = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(contract)

ticker = ib.reqMktData(contract, '', False, False)
ib.sleep(2)

print('Last:', ticker.last, ' Bid:', ticker.bid, ' Ask:', ticker.ask)

ib.disconnect()
