import pandas_datareader.data as pdr
import datetime
import tkinter 

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2018, 7, 7)

# f = web.DataReader('F', 'google', start, end)

f = pdr.get_data_yahoo('BABA',start,end)

print(f.ix['2018-01-04'])



# from pandas_datareader import data as pdr
import plotly.offline as py_offline
import plotly.graph_objs as go
import fix_yahoo_finance as yf

py_offline.init_notebook_mode(connected=True)

yf.pdr_override()
mcd = pdr.get_data_yahoo("MCD", start="2005-07-01", end="2005-07-31")
mcd_candle = go.Candlestick(x=mcd.index,
                            open=mcd.Open,
                            high=mcd.High,
                            low=mcd.Low,
                            close=mcd.Close,
                            increasing=dict(line=dict(color= '#00FF00')),
                            decreasing=dict(line=dict(color= '#FF0000'))
                           )
data = [mcd_candle]

layout = go.Layout(
    plot_bgcolor='rgb(59,68,75)'
)

fig = go.Figure(data=data, layout=layout)
