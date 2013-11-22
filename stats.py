import sys
from datetime import datetime, date, time

def avg_time(datetimes):
  previous = None
  deltas = []
  for dt in datetimes:
    if (previous):
      d = dt - previous
      deltas.append(divmod(d.days * 86400 + d.seconds, 60))
    previous = dt

  return deltas

with open(".trails","r") as theFile:
  fmt   = '%d %B %Y %H:%M:%S'
  times = []
  for line in theFile:
    data = line.split(' ->')[0]
    ts = datetime.strptime(data, fmt)
    times.append(ts)

  print(avg_time(times))
