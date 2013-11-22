import sys
from datetime import datetime, date, time

def avg_time(datetimes):
  previous = None
  deltas = []
  for dt in datetimes:
    if previous:
      d = dt - previous
      deltas.append(divmod(d.days * 86400 + d.seconds, 60))
    previous = dt

  mins = sum([v[0] for v in deltas]) / len(deltas)
  sec  = sum([v[1] for v in deltas]) / len(deltas)
  return mins, sec

with open(".trails","r") as theFile:
  fmt   = '%d %B %Y %H:%M:%S'
  times = []
  counter = 0
  for line in theFile:
    counter += 1
    data = line.split(' ->')[0]
    ts = datetime.strptime(data, fmt)
    times.append(ts)

  avg = avg_time(times)
  print('\n  [ %d mins %d sec ]\tYour average time between trails' % (avg[0], avg[1]) )
  print('  [ %d ]\t\ttrails created so far in this project.' % counter )
