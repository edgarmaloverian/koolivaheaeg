# eeschoolbreak small library signalling if some date is chhool break in Estonia
from datetime import date

vaheajad = [
    ["Talvevaheaeg 2022", 22, 12, 2022, 8,  1, 2023],
    ["Suusavaheaeg 2023", 27, 2,  2023, 5,  3, 2023],
    ["Kevadvaheaeg 2023", 24, 4,  2023, 30, 4, 2023],
    ["Suvevaheaeg 2023",  14, 6,  2023, 31, 8, 2023]
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