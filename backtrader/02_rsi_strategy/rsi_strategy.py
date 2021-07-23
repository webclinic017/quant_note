# -*- coding: utf-8 -*-
# @Author: zhouhy
# @Date:   2021-07-21 16:36:51
# @Last Modified by:   zhou
# @Last Modified time: 2021-07-23 09:51:42
import backtrader as bt
import datetime
import backtrader.feeds as btfeeds
import pandas as pd
class mystrategy(bt.Strategy):
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        time=self.datas[0].datetime.time()
        print('%s, %s, %s' % (dt.isoformat(), time, txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
        # Add a MovingAverageSimple indicator
        # Indicators for the plotting show
        self.rsi = bt.indicators.RSI_SMA(self.data.close,period=50)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))
    def next(self):

        if self.order:
            return

        if self.data.datetime.time()<datetime.time(14,55):
            if not self.position:
                if self.rsi>70:
                    self.order=self.sell()
                if self.rsi<30:
                    self.order=self.buy()

            else:
                if self.position.size==1:
                    profit=self.dataclose[0]-self.position.price
                    if profit>40 and profit<-5:
                        self.order=self.close()
                elif self.position.size==-1:
                    profit=-self.dataclose[0]+self.position.price
                    if profit>40 and profit<-5:
                        self.order=self.close()
                else:
                    pass
        
        if self.data.datetime.time()>datetime.time(14,55):
            if self.position.size!=0:
                self.order=self.close()


df=pd.read_csv("IF.csv")
df.index=pd.to_datetime(df["DATETIME"])
df.drop(["DATETIME"],axis=1,inplace=True)
data=btfeeds.PandasData(dataname=df,fromdate=datetime.datetime(2020, 10, 1),todate=datetime.datetime(2020, 12, 31))
cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.broker.setcash(1000000.0)
cerebro.addstrategy(mystrategy)
cerebro.broker.setcommission(commission=2.5,margin=117000, mult=300.0)
print('Start Value: {}'.format(cerebro.broker.getvalue()))
cerebro.run()
print('Final Value: {}'.format(cerebro.broker.getvalue()))
cerebro.plot(style="candlestick")
