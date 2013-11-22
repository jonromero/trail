import sys
import time, datetime
with open(".trails","r") as theFile:
  fmt = '%d %B %Y %H:%M:%S'
  for line in theFile:
    data = line.split('->')[0]
    try:
      data = time.strptime(data, fmt)
    except ValueError, v:
      if len(v.args) > 0 and v.args[0].startswith('unconverted data remains: '):
          data = data[:-(len(v.args[0])-26)]
          data = time.strptime(data, fmt)
      else:
          raise v
    print(data)
