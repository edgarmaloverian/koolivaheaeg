# eeschoolbreak small library signalling if some date is chhool break in Estonia
# source https://www.riigiteataja.ee/akt/110092020003?leiaKehtiv

from datetime import date

vaheajad = [
    ["II vaheaeg 2022/3", 22, 12, 2022, 8,  1, 2023],
    ["III vaheaeg 2022/3", 27, 2,  2023, 5,  3, 2023],
    ["IV vaheaeg 2022/3", 24, 4,  2023, 30, 4, 2023],
    ["V vaheaeg 2022/3",  14, 6,  2023, 31, 8, 2023],
    ["I vaheaeg 2023/4", 23, 10, 2023, 29, 10, 2023],
    ["II vaheaeg 2023/4", 21, 12, 2023, 7, 1, 2024],
    ["III vaheaeg 2023/4", 26, 2, 2024, 3, 3, 2024],
    ["IV vaheaeg 2023/4", 22, 4, 2024, 28, 4, 2024],
    ["V vaheaeg 2023/4", 13, 6, 2024, 31, 8, 2024],
]
            
def isbreak(a=date.today()): # returns True if it is break today, if you want it to pass another date you need to write argparser
    sb = False
    for i in range(len(vaheajad)):
      if (a > date(vaheajad[i][3],vaheajad[i][2],vaheajad[i][1]) and a < date(vaheajad[i][6],vaheajad[i][5],vaheajad[i][4])):  
        sb = True
    return sb

def breaks(): # returns list of breaks
  for i in range(len(vaheajad)):
    print(vaheajad[i])