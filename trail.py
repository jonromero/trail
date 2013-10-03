#!/usr/bin/env python
"""Jot down your thoughts during development"""

from datetime import datetime
import json
from optparse import OptionParser
FILENAME = ".trails"

def save(trails):
    with open(FILENAME, "w") as trail_file:
        trail_file.write(json.dumps(trails))
        print "trail added"

def load():
    try:
        fd = open(FILENAME, "r")
        trails = fd.read()
        fd.close()
        return json.loads(trails)        
    except IOError:
        print "File", FILENAME, "does not exist in the current directory"
        return {}
    except ValueError:
        print "File", FILENAME, "is not valid"
        exit(1)


def print_list(trails, num_of_last_trails):
    """
    Print the last num_of_last_trails 
    """
    #for trail in reversed(trails[-num_of_last_trails:]):
    trails.keys().sort(key=lambda x: x, reverse=True)
    for tkey in sorted_keys:
        print "%s: %s" % (tkey, trails[tkey])

        
def parser():
    """Return a parser for the command-line interface."""
    usage = "Usage: %prog [-l number_of_last_trails] [TEXT]"
    parser = OptionParser(usage=usage)

    parser.add_option("-l", "--list", dest="tail_num", type="int",
                      help="list latest N trails")

    return parser

def go():
    """ Run command-line  """
    (options, args) = parser().parse_args()

    text = ' '.join(args).strip()
    trails = load()
    
    if options.tail_num:
        print_list(trails, options.tail_num)
    elif text.strip(" "):
        new_trail = {datetime.now().strftime("%d %B %Y %H:%M"): text}
        trails.update(new_trail)
        save(trails)
    else:
        parser().print_help()


if __name__ == '__main__':
    go()
