import sys
import time, datetime
with open(".trails","r") as theFile:
  fmt   = '%d %B %Y %H:%M:%S'
  times = []
  for line in theFile:
    data = line.split(' ->')[0]
    ts = time.strptime(data, fmt)
    times.append(ts)

  print(times)
