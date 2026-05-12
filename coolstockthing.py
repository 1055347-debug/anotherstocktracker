import yfinance
import statistics
import pandas
what1 = input("What stock did you buy?: ")
what2 = input("What year did you buy the stock?: ")
what3 = input("What month did you buy your stock?: ")
what4 = input("What day did you buy your stock?: ")
coolio1 = int(what3)
coolio2 = int(what4)
month = f"{coolio1:02}"
day = f"{coolio2:02}"
there = what2 + "-" + month + "-" + day
hello = int(day)
day2 = str(hello + 1)
day1 = what2 + "-" + month + "-" + day2
data = yfinance.download(what1, start=there, end=day1)
gh = data["Close"][what1].tolist()
data2 = yfinance.download(what1, period="1mo")
structure = data2.tail(1)
structure2 = structure["Close"][what1].tolist()
finalthing = structure2[0] - gh[0]
print(gh)
print(finalthing)
what5 = input("Now are there any stocks you are looking into buying? ")
data3 = yfinance.download(what5, period="6mo")
#print(data3.columns)
print(data3["Close"])
idk2 = data3.head(1)
structure3 = idk2["Close"][what5].tolist()
data4 = yfinance.download(what5, period="1mo")
idk3 = data4.tail(1)
structure4 = idk3["Close"][what5].tolist()
hellothere = structure4[0] - structure3[0]
finalthing2 = hellothere /  structure3[0]
print(finalthing2)