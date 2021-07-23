import backtrader as bt
import datetime
class mystrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        print(self.datas[0].datetime.date(0),self.dataclose[0])

cerebro = bt.Cerebro()
datapath="orcl-1995-2014.txt"
data = bt.feeds.YahooFinanceCSVData(dataname=datapath,fromdate=datetime.datetime(2000, 1, 1),todate=datetime.datetime(2000, 12, 31),reverse=False)
cerebro.adddata(data)
cerebro.addstrategy(mystrategy)
print('Start Value: {}'.format(cerebro.broker.getvalue()))
cerebro.run()
print('Final Value: {}'.format(cerebro.broker.getvalue()))
cerebro.plot()