import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

def askInput():
    tickerNames = []
    again = True
    asking = True
    while asking:
        ticker = input('Name (TICKER NAME): ')
        tickerNames.append(ticker)
        again = input('Add another? (Y/N): ').lower()
        if again != 'y':
            asking = False
    
    return tickerNames

def makeGraph(names):

    dataArray = []

    plt.figure(figsize=(12, 6))

    for name in range(len(names)):
        data = yf.download(names[name], start='2023-01-01', end='2024-07-24')
        dataArray.append(data)
    
    for dataItem in dataArray:
        dataItem.index = pd.to_datetime(dataItem.index)

    index = 0

    for item in dataArray:
        plt.plot(item['Close'], label = names[index])
        index += 1

        

def showGraph():
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Tech companies stock price')
    plt.legend()
    plt.grid(True)
    plt.show()


def run():
        
    tickerNames = askInput()

    makeGraph(tickerNames)
    showGraph()

run()