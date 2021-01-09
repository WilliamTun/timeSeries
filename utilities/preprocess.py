def percentChange(startPoint,currentPoint):
    return ((currentPoint-startPoint)/startPoint)*100.00

def movingAverage(timeSeries, timeFrame): 
    return timeSeries.rolling(window=timeFrame).mean()